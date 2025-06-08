import threading
import random
import timeit
import xml.etree.ElementTree as ET
import cv2
from cv2.typing import MatLike
import pytesseract
import imutils
from config import ROOT_PATH, ANNOTATIONS_FILE, CHARS_MAP
from detect import predict
from utils import replace_chars


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


def process_image(img: MatLike) -> tuple[str, str]:
    """
    Function processing given cropped image, retrieving
    and cleaning up license plate numbers from it.

    Parameters:
        img (MatLike): cropped image of license plate

    Returns:
        result (tuple[str, str]): tuple of non-cleaned up and cleaned up license plate numbers
    """
    img = imutils.resize(img, width=500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 41, 21)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    inv = cv2.bitwise_not(thresh)
    config = "--oem 3 --psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    plate_number = pytesseract.image_to_string(inv, config=config)
    unpr_text = plate_number.strip()
    # assuming we detect POLISH license plates (!!!) and that we only read plates for recognision
    pr_text = process_text(unpr_text)
    return unpr_text, pr_text


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
    random.shuffle(data)
    return data[:n]


def read_plate(img_name: str) -> tuple[str, str]:
    """
    Function reading license plate number from an image.

    Parameters:
        img_name (str): name of image to be processed

    Returns:
        result (tuple[str, str]): tuple of non-cleaned up and cleaned up license plate numbers
    """
    img_path = f"{ROOT_PATH}data/photos/{img_name}"
    coord = predict(img_path)
    if not coord:
        return ("", "")
    xtl, ytl, xbr, ybr = coord
    crop = cv2.imread(img_path)[ytl:ybr, xtl:xbr]
    unpr_plate_num, pr_plate_number = process_image(crop)
    return unpr_plate_num, pr_plate_number


def run(data: list[MatLike]) -> int:
    """
    Function firing up detection and OCR on list of images
    and counting number of good readings.

    Parameters:
        data (list[MatLike]): list of images to be processed

    Returns:
        result (int): number of good results
    """
    good = 0
    for img, num in data:
        res = read_plate(img)
        if not res:
            continue
        if num in res[0] or num in res[1]:
            good += 1
    return good


def calculate_final_grade(accuracy_percent: float, processing_time_sec: float) -> float:
    """
    Calculates the final grade based on license plate OCR accuracy and processing time.
    Parameters:
    - accuracy_percent: OCR accuracy as a percentage (0–100)
    - processing_time_sec: total time to process 100 images in seconds
    Returns:
    - Grade on a scale from 2.0 to 5.0 (rounded to the nearest 0.5)
    """
    if accuracy_percent < 60 or processing_time_sec > 60:
        return 2.0
    accuracy_norm = (accuracy_percent - 60) / 40
    time_norm = (60 - processing_time_sec) / 50
    score = 0.7 * accuracy_norm + 0.3 * time_norm
    grade = 2.0 + 3.0 * score
    print(grade)
    return round(grade * 2) / 2


def worker(subdata: list[MatLike], results: list[int]) -> None:
    """
    Function starting multithreading worker.

    Parameters:
        subdata (list[MatLike]): subset of list of images to process

        resutls (list[int]): reference to list of worker results
    """
    results.append(run(subdata))


if __name__ == "__main__":
    DATA_SIZE = 100
    NUM_THREADS = 4
    data = get_plate_data(f"{ROOT_PATH}data/{ANNOTATIONS_FILE}", DATA_SIZE)

    chunk_size = len(data) // NUM_THREADS
    threads = []
    results = []

    s = timeit.default_timer()

    for i in range(NUM_THREADS):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != NUM_THREADS - 1 else len(data)
        thread = threading.Thread(target=worker, args=(data[start:end], results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    e = timeit.default_timer()
    time_exec = e - s
    acc = sum(results) / DATA_SIZE

    print(f"accuracy: {acc * 100:.2f}%")
    print(f"exec time: {time_exec:.2f}s")
    print(f"grade: {calculate_final_grade(acc * 100, time_exec)}")
