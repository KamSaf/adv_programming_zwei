from ultralytics import YOLO
import cv2


def predict(
    img_path: str,
    weights: str = "runs/detect/train/weights/best.pt",
    show_result: bool = False,
) -> list:
    model = YOLO(weights)
    results = model.predict(source=img_path, verbose=False)[0]
    if show_result:
        img = cv2.imread(img_path)
        xtl, ytl, xbr, ybr = map(int, results.boxes.xyxy[0])
        cv2.rectangle(img, (xtl, ytl), (xbr, ybr), (0, 255, 0), 3)
        res_img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
        cv2.imshow("Image with bbox", res_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return (xtl, ytl, xbr, ybr)


if __name__ == "__main__":
    print(predict("../data/photos/110.jpg", show_result=True))
