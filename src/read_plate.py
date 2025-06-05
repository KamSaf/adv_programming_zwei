import timeit
import xml.etree.ElementTree as ET
from typing import Tuple
import numpy as np
import cv2
from cv2.typing import MatLike
import pytesseract
from config import ROOT_PATH
from detect import predict
import imutils


def remove_heavy_dark_regions(img: MatLike, area_threshold: int = 1000) -> MatLike:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, dark_mask = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(
        dark_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    mask = np.ones_like(gray, dtype=np.uint8) * 255
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > area_threshold:
            cv2.drawContours(mask, [cnt], -1, 1, -1)
    result = cv2.bitwise_and(img, img, mask=mask)
    return result


def process_image(img: MatLike) -> Tuple[str, MatLike]:
    # find_plate(img)
    img = imutils.resize(img, width=500)
    cleaned = remove_heavy_dark_regions(img)
    gray = cv2.cvtColor(cleaned, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 41, 21)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    inv = cv2.bitwise_not(thresh)
    config = "--oem 3 --psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    plate_number = pytesseract.image_to_string(inv, config=config)
    return plate_number.strip(), inv


def get_plate_data(xml_path: str) -> None:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data = [
        (image.attrib["name"], image.find("box").find("attribute").text)
        for image in root
        if image.tag == "image"
    ]
    return data


def read_plate(img_name: str) -> str:
    img_path = f"{ROOT_PATH}data/photos/{img_name}"
    coord = predict(img_path)
    if not coord:
        return ""
    xtl, ytl, xbr, ybr = coord
    crop = cv2.imread(img_path)[ytl:ybr, xtl:xbr]
    plate_num, p_crop = process_image(crop)
    return plate_num


def run() -> None:
    data = get_plate_data("../data/annotations.xml")
    good = 0
    bad = 0
    for i, (img, num) in enumerate(data):
        if i > 99:
            break
        if num in read_plate(img):
            good += 1
        else:
            bad += 1
    return good / (good + bad)


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


if __name__ == "__main__":
    s = timeit.default_timer()
    acc = run()
    e = timeit.default_timer()
    time = e - s
    print(f"accuracy: {acc*100}")
    print(f"exec time: {time}")
    print(f"grade: {calculate_final_grade(acc*100, time)}")
