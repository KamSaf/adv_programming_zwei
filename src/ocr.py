import cv2
from cv2.typing import MatLike
import pytesseract
import imutils
from config import DATASET_PATH
from detect import predict


def process_image(img: MatLike) -> str:
    """
    Function processing given cropped image, retrieving
    and cleaning up license plate numbers from it.

    Parameters:
        img (MatLike): cropped image of license plate

    Returns:
        text (str): retrieved license plate number
    """
    img = imutils.resize(img, width=500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 41, 21)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    inv = cv2.bitwise_not(thresh)
    config = "--oem 3 --psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    plate_number = pytesseract.image_to_string(inv, config=config)
    text = plate_number.strip()
    return text


def read_plate(img_name: str) -> tuple[tuple[str, str], float]:
    """
    Function reading license plate number from an image.

    Parameters:
        img_name (str): name of image to be processed

    Returns:
        num_plate (str): license plate number
    """
    img_path = f"{DATASET_PATH}{img_name}"
    coord, iou = predict(img_path)
    if not coord:
        return ("", "")
    xtl, ytl, xbr, ybr = coord
    crop = cv2.imread(img_path)[ytl:ybr, xtl:xbr]
    return process_image(crop), iou


if __name__ == "__main__":
    print(read_plate("52.jpg"))
