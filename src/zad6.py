import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../images/dude.jpg", cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
_, otsu_thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

otsu_value = int(_)
plt.figure(figsize=(10, 5))
plt.title("gray scale otsu threshold hist")
plt.plot(hist, color="black")
plt.axvline(
    x=otsu_value, color="red", linestyle="--", label=f"otsu thresh = {otsu_value}"
)
plt.xlabel("gray level")
plt.ylabel("pixel number")
plt.legend()
plt.grid(True)
plt.show()

# cv2.imshow("hist", otsu_thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
