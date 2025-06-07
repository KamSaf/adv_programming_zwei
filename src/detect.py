from ultralytics import YOLO
import cv2
from utils import resize_img


def predict(
    img_path: str,
    weights: str = "runs/detect/train/weights/best.pt",
    show_result: bool = False,
) -> tuple[float, float, float, float] | None:
    """
    Function predicting coordinates of the license plate
    bounding box on given image.

    Parameters:
        img_path (str): path to image which is to be processed

        weights (str): path to YOLO11n weights (optional)

        show_result (bool): bool flag determining whether image with marked bbox should be displayed

    Returns:
        result (tuple[float, float, float, float] | None):
        tuple with bbox coordinates or None if bbox was not found

    """
    model = YOLO(weights)
    results = model.predict(source=img_path, verbose=False)[0]
    if not results:
        return None
    xtl, ytl, xbr, ybr = map(int, results.boxes.xyxy[0])
    if show_result:
        img = cv2.imread(img_path)
        cv2.rectangle(img, (xtl, ytl), (xbr, ybr), (0, 255, 0), 3)
        res_img = resize_img(img)
        cv2.imshow("Image with bbox", res_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return (xtl, ytl, xbr, ybr)


if __name__ == "__main__":
    print(predict("../data/photos/110.jpg", show_result=True))
