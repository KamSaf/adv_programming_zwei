import sys
import cv2

image = cv2.imread("../images/joe.jpg")

try:
    angle = int(input("Enter angle degrees value:\n"))
except Exception:
    print("Invalid data entered")
    sys.exit()

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow(f"Joe Rotated by {angle} Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
