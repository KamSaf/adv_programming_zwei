import os
from shutil import copyfile
from cv2 import resize
from cv2.typing import MatLike
from config import ROOT_PATH


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
        result (float): normalised dimension of a figure
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
        result (float): normalised center of figure dimension

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
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


def copy_dataset(
    src: str,
    file_names: list[str],
    dest: str,
    labels_path: str = ROOT_PATH + "data/labels/",
) -> None:
    """
    Function copying given images with their labels to new directory.

    Parameters:
        src (str): path to directory containing dataset

        file_names (str): list of images names to be copied

        dest (str): path to directory where dataset is to be placed

        labels_path (str): path to directory containing .txt labels
    """
    purge_dir(dest)
    for file_n in file_names:
        copy_file(src + file_n, dest + file_n)
        label_name = file_n[:-3] + "txt"
        copy_file(labels_path + label_name, dest + label_name)


def resize_img(img: MatLike, multipl: int = 4) -> MatLike:
    return resize(img, (img.shape[1] // multipl, img.shape[0] // multipl))
