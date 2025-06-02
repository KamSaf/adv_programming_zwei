import cv2


def resize(image):
    h, w = image.shape[:2]
    return cv2.resize(image, (int(w / 4), int(h / 4)))


image = cv2.imread("../images/klocki.jpg")
template = cv2.imread("../images/klocek.jpg")
cv2.imshow("Image", image)
cv2.imshow("Template", template)
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
(startX, startY) = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]
cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)
cv2.imshow("Output", image)
cv2.waitKey(0)
