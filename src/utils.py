import os
import random
import xml.etree.ElementTree as ET
from shutil import copyfile
from cv2 import resize
from cv2.typing import MatLike
from config import CHARS_MAP, REV_CHARS_MAP, LABELS_PATH


def create_dir(directory: str) -> None:
    """
    Function creating new directory.

    Parameters:
        directory (str): directory of a directory to be created
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def norm_size(c1: str, c2: str, dim: str) -> float:
    """
    Function normalizing size of a bounding box with image size.

    Parameters:
        c1 (str): starting point of a figure

        c2 (str): ending point of a figure

        dim (str): dimension of an image

    Returns:
        norm_size (float): normalised dimension of a figure
    """
    f_c1, f_c2, f_dim = map(float, (c1, c2, dim))
    return (f_c2 - f_c1) / f_dim


def norm_coord(c1: str, c2: str, dim: str) -> float:
    """
    Function calculating and normalising center point dimension
    of a figure with image size.

    Parameters:
        c1 (str): starting point of a figure

        c2 (str): ending point of a figure

        dim (str): dimension of and image

    Returns:
        norm_coord (float): normalised center of figure dimension

    """
    f_c1, f_c2, f_dim = map(float, (c1, c2, dim))
    return ((f_c2 + f_c1) / 2) / f_dim


def copy_file(src: str, dest: str) -> None:
    """
    Function copying file from source to
    destination directory.

    Parameters:
        src (str): path to file which is to be copied

        dest (str): path of destination (including file name)
    """
    dir = "/".join(dest.split("/")[:-1])
    create_dir(dir)
    copyfile(src, dest)


def purge_dir(path: str) -> None:
    """
    Function deleting all content from a directory.

    Parameters:
        path (str): path to directory which is to be purged
    """
    for filename in os.listdir(path):
        file_path = path + filename
        if os.path.isfile(file_path):
            os.remove(file_path)


def copy_dataset(
    src: str,
    file_names: list[str],
    dest: str,
    labels_path: str = LABELS_PATH,
) -> None:
    """
    Function copying given images with their labels to new directory.

    Parameters:
        src (str): path to directory containing dataset

        file_names (str): list of images names to be copied

        dest (str): path to directory where dataset is to be placed

        labels_path (str): path to directory containing .txt labels
    """
    create_dir(LABELS_PATH)
    purge_dir(dest)
    for file_n in file_names:
        copy_file(src + file_n, dest + file_n)
        label_name = file_n[:-3] + "txt"
        copy_file(labels_path + label_name, dest + label_name)


def shrink_img(img: MatLike, n: int = 4) -> MatLike:
    """
    Function decreasing images size n times in both dimensions.

    Parameters:
        img (MatLike): image to be resized

        multipl (int): reduce modifier

    Returns:
        shrinked_image (MatLike): image shrinked n times in both dimensions
    """
    return resize(img, (img.shape[1] // n, img.shape[0] // n))


def shuffle(data: list[str]) -> None:
    # BEST 9000
    # WORST 8675309
    random.seed(random.choice((98765, 123, 9000)))
    random.shuffle(data)


def get_plate_data(xml_path: str, n: int = 100) -> list[MatLike]:
    """
    Function preparing dataset to perform detection.

    Parameters:
        xml_path (str): path to .xml file with annotations

        n (int): length of images list to be processed
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data = [
        (image.attrib["name"], image.find("box").find("attribute").text)
        for image in root
        if image.tag == "image"
    ]
    shuffle(data)
    return data[:n]


def replace_chars(text: str, split: int | None, rev: bool = False) -> str:
    """
    Function replacing characters with their corresponding equivalents
    defined in maps defined in config.py in whole string or substring
    defined with split value.

    Parameters:
        text (str): original text to be processed

        split (int): index by which text is to be split (if not given then whole text is processed)

        rev (bool): if set to True then reverse char map is used (chars to numbers)

    Returns:
        repl_text (str): text with replaced characters
    """
    if split > len(text):
        return text
    c_map = CHARS_MAP if not rev else REV_CHARS_MAP
    if split is None:
        for c in text:
            if c not in c_map.keys():
                continue
            text = text.replace(c, c_map[c])
        return text
    for i, c in enumerate(text[:split]):
        if c in c_map.keys():
            text = "".join([text[:split].replace(c, CHARS_MAP[c]), text[split:]])
    return text


def process_text(text: str) -> str:
    """
    Function cleaning up recognised license plate number utilising rules
    which apply in polish license plate numbers.

    Parameters:
        text (str): text to be cleaned up

    Returns:
        result (str): cleaned up text after rules application
    """
    if len(text) < 4:
        return ""
    while len(text) > 8 and text[0] in "0123456789":
        text = CHARS_MAP[text[0]] + text[1:]
        if text[0] in "AIM0123456789" or (text[1:3] != "BI" and text[0] == "B"):
            text = text[1:]
    while text[0] in "AIM0123456789" or (text[1:3] != "BI" and text[0] == "B"):
        text = text[1:]
    if len(text) == 8:
        text = replace_chars(text, 3)
    if len(text) == 7:
        text = replace_chars(text, 2)
    return text


def evaluate(plate_num: str, ocr_res: str) -> bool:
    """
    Function determining whether OCR result matches
    real license plate number.

    Parameters:
        plate_num (str): real license plate number

        ocr_res (str): result of OCR operation

    Returns:
        match (bool): comparison result
    """
    cleaned_up_text = process_text(ocr_res)
    return plate_num in ocr_res or plate_num in cleaned_up_text
