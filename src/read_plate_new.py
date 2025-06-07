import threading
from queue import Queue
import random
import timeit
import xml.etree.ElementTree as ET
from typing import Tuple
import cv2
from cv2.typing import MatLike
import pytesseract
import imutils
from config import ROOT_PATH, ANNOTATIONS_FILE, CHARS_MAP, REV_CHARS_MAP
from detect import predict


def replace_chars(text: str, split: int | None, rev: bool = False) -> str:
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
    if len(text) < 4:
        return ""
    if text[0] in "AIM0123456789":
        text = text[1:]
    if text[0:3] != "BI" and text[0] == "B":
        text = text[1:]
    if text[0] in CHARS_MAP.keys():
        text = "".join([CHARS_MAP[text[0]], text[1:]])
    if text[:2].isalnum() and not text[2].isalnum() and len(text) > 7:
        text = text[:8]
    elif text[:3].isalnum() and len(text) > 8:
        text = text[:8]
    if len(text) > 1 and text[0] in "AIM0123456789":
        text = text[1:]
    if len(text) > 8:
        text = text[:8]
    if len(text) > 7:
        replace_chars(text, 3)
    elif len(text) > 6:
        replace_chars(text, 2)
    if len(text) > 0 and text[:2].isalnum() and not text[2].isalnum():
        text = text[:7]
    if len(text) == 7 and text[0].isalnum() and not text[1].isalnum():
        text = "".join([text[0], CHARS_MAP[text[1]], text[2:]])
    if len(text) > 7 and text[:3].isalnum() and not text[3].isalnum():
        text = text[:8]
    if len(text) == 8:
        text = replace_chars(text, 3)
    if len(text) == 7:
        text = replace_chars(text, 2)
    if text[:2].isalnum():
        text
    if text[:2].isalnum():
        text
    return text


def process_image(img: MatLike) -> Tuple[str, MatLike]:
    # assuming we detect POLISH license plates (!!!) and that we only read plates for recognision
    img = imutils.resize(img, width=500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 41, 21)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    inv = cv2.bitwise_not(thresh)
    config = "--oem 3 --psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    plate_number = pytesseract.image_to_string(inv, config=config)
    unpr_text = plate_number.strip()
    for i in range(2):
        pr_text = process_text(unpr_text)
    return unpr_text, pr_text, inv


def get_plate_data(xml_path: str, n: int = 100) -> None:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data = [
        (image.attrib["name"], image.find("box").find("attribute").text)
        for image in root
        if image.tag == "image"
    ]
    random.shuffle(data)
    return data[:n]


def read_plate(img_name: str) -> str:
    img_path = f"{ROOT_PATH}data/photos/{img_name}"
    coord = predict(img_path)
    if not coord:
        return ""
    xtl, ytl, xbr, ybr = coord
    crop = cv2.imread(img_path)[ytl:ybr, xtl:xbr]
    unpr_plate_num, pr_plate_number, _ = process_image(crop)
    return unpr_plate_num, pr_plate_number


def run(data: list, n: int = 100) -> None:
    good = 0
    for img, num in data:
        res = read_plate(img)
        if not res:
            continue
        res1, res2 = res[0], res[1]
        if num in res1 or num in res2:
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


def worker(subdata, results, data_size):
    acc = run(subdata, data_size)
    results.append(acc)


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
        thread = threading.Thread(
            target=worker, args=(data[start:end], results, DATA_SIZE / NUM_THREADS)
        )
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
