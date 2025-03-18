import cv2


image = cv2.imread("../images/joe.jpg")
h, w = image.shape[:2]

for i, m in enumerate((cv2.INTER_CUBIC, cv2.INTER_LANCZOS4)):
    resized = cv2.resize(image, (w * 4, h * 4), interpolation=m)
    cv2.imshow(f"Resized Joe {i + 1}", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
