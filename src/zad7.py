import cv2

img = cv2.imread("../images/screenshot.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template_x, template_y, template_w, template_h = 100, 150, 32, 32
template = gray[
    template_y : template_y + template_h, template_x : template_x + template_w
]

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w < 10 or h < 10 or w > 100 or h > 100:
        continue
    roi = gray[y : y + h, x : x + w]
    try:
        roi_resized = cv2.resize(roi, (template.shape[1], template.shape[0]))
    except Exception:
        continue
    result = cv2.matchTemplate(roi_resized, template, cv2.TM_CCOEFF_NORMED)
    similarity = result[0][0]
    if similarity >= 0.8:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            img,
            f"{similarity:.2f}",
            (x, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (0, 255, 0),
            1,
        )
cv2.imshow("Dopasowane obiekty", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
