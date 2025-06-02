import cv2
import numpy as np

screenshot = cv2.imread("../images/pulpit.jpg")
gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
x, y, w, h = 100, 150, 32, 32
template = gray_screenshot[y : y + h, x : x + w]
res = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
cv2.imshow("Detected Icons", screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()
