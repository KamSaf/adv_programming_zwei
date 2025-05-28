import cv2


def process_image(img):
    blurred = cv2.GaussianBlur(img, (7, 7), 0)
    eroded = cv2.erode(blurred.copy(), None, iterations=5)
    (T, threshInv) = cv2.threshold(eroded, 100, 255, cv2.THRESH_BINARY_INV)
    return threshInv


image = cv2.imread("../images/dude.jpg")
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
light_gray = cv2.add(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 50)
cv2.imshow("gray", process_image(gray))
cv2.imshow("gray with increased brightness", process_image(light_gray))
cv2.waitKey(0)
cv2.destroyAllWindows()
