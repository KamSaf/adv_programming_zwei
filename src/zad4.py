import cv2


def resize(image):
    h, w = image.shape[:2]
    return cv2.resize(image, (int(w / 4), int(h / 4)))


for method in (
    cv2.TM_CCOEFF,
    cv2.TM_CCOEFF_NORMED,
    cv2.TM_CCORR,
    cv2.TM_CCORR_NORMED,
    cv2.TM_SQDIFF,
    cv2.TM_SQDIFF_NORMED,
):
    for i in (1, 2, 3, 4, 5):
        path = f"../images/fanta_{i}."
        if i == 4:
            path += "png"
        else:
            path += "jpg"
        image = cv2.imread(path)
        if i == 1:
            image = resize(image)
        template = cv2.imread("../images/fanta_etykieta.jpg")
        cv2.imshow("Image", image)
        cv2.imshow("Template", template)
        imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(imageGray, templateGray, method)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
        (startX, startY) = maxLoc
        endX = startX + template.shape[1]
        endY = startY + template.shape[0]
        cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)
        cv2.imshow(f"Output (method: {method})", image)
        cv2.waitKey(0)
