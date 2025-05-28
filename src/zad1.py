import cv2

image = cv2.imread("../images/dude.jpg")
cv2.imshow("og image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
for t in (30, 100, 200):
    (T, threshInv) = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("threshold binary inverse", threshInv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
