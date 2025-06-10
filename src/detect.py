import xml.etree.ElementTree as ET
import cv2
from ultralytics import YOLO
from utils import shrink_img
from config import WEIGHTS_PATH, DATASET_PATH, ANNOTATIONS_FILE


def calculate_iou(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    interArea = max(0, xB - xA) * max(0, yB - yA)
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    return interArea / float(boxAArea + boxBArea - interArea)


def get_bbox(img_name: str) -> tuple[float, ...]:
    xml_path = ANNOTATIONS_FILE
    tree = ET.parse(xml_path)
    root = tree.getroot()
    bbox = (0, 0, 0, 0)
    for image in root:
        if image.tag != "image" or image.attrib["name"] != img_name:
            continue
        box = image.find("box")
        bbox = tuple(
            [float(box.attrib[coord]) for coord in ("xtl", "ytl", "xbr", "ybr")]
        )
    return bbox


def predict(
    img_path: str,
    weights: str = WEIGHTS_PATH,
    show_result: bool = False,
) -> tuple[tuple[float, float, float, float] | None, float]:
    """
    Function predicting coordinates of the license plate
    bounding box on given image.

    Parameters:
        img_path (str): path to image which is to be processed

        weights (str): path to YOLO11n weights

        show_result (bool): bool flag determining whether image with marked bbox should be displayed

    Returns:
        bbox_coord (tuple[float, float, float, float] | None):
        tuple with bbox coordinates or None if bbox was not found
    """
    model = YOLO(weights)
    results = model.predict(source=img_path, verbose=False)[0]
    if not results:
        return None, 0
    xtl, ytl, xbr, ybr = map(int, results.boxes.xyxy[0])
    img_name = img_path.split("/")[-1]
    true_bbox = get_bbox(img_name)
    iou = calculate_iou(true_bbox, (xtl, ytl, xbr, ybr))
    if show_result:
        img = cv2.imread(img_path)
        cv2.rectangle(img, (xtl, ytl), (xbr, ybr), (0, 255, 0), 3)
        res_img = shrink_img(img)
        cv2.imshow("Image with bbox", res_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return (xtl, ytl, xbr, ybr), iou


if __name__ == "__main__":
    print(predict(f"{DATASET_PATH}110.jpg", show_result=True))
