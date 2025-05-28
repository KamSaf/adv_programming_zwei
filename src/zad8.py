import cv2


def thresholding(img):
    (_, threshInv) = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
    (T, threshOtsu) = cv2.threshold(
        img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
    )
    cv2.imshow("threshold binary inverse", threshInv)
    cv2.imshow(f"threshold otsu (T = {T})", threshOtsu)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image = cv2.imread("../images/kostka.png")
cv2.imshow("image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
eroded = cv2.erode(blurred.copy(), None, iterations=1)
thresholding(gray)
thresholding(eroded)
