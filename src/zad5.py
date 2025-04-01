import numpy as np
import cv2

# image = cv2.imread("../images/bad_guy_staring.jpg")
# image = cv2.imread("../images/opencv_logo.png")
image = cv2.imread("../images/jeep.jpg")
cv2.imshow("original", image)

# red
lower_bound = np.array((125, 50, 0))
upper_bound = np.array((255, 255, 255))

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lowerb=lower_bound, upperb=upper_bound)
mask_inv = cv2.bitwise_not(mask)
masked = cv2.bitwise_and(image, image, mask=mask)

# increasing saturation
imghsv = cv2.cvtColor(masked, cv2.COLOR_BGR2HSV).astype("float32")
(h, s, v) = cv2.split(imghsv)
s = s * 2
s = np.clip(s, 0, 255)
imghsv = cv2.merge([h, s, v])
imgrgb = cv2.cvtColor(imghsv.astype("uint8"), cv2.COLOR_HSV2BGR)

background = cv2.bitwise_and(image, image, mask=mask_inv)
result = cv2.add(imgrgb, background)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
