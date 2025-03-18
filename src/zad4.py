import cv2


image = cv2.imread("../images/joe.jpg")
h, w = image.shape[:2]
methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_AREA", cv2.INTER_AREA),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
    ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4),
]
for n, m in methods:
    resized = cv2.resize(image, (w * 3, h * 3), interpolation=m)
    cv2.imshow(f"Resized Joe {n}", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
