import cv2

image = cv2.imread("../images/dude.jpg")
cv2.imshow("og image", image)
gray = cv2.add(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 50)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
(T, thresh) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("threshold", thresh)
print("otsu thresholding value: {}".format(T))
cv2.waitKey(0)
