import cv2

PATH = "../images/opencv_logo.png"
image = cv2.imread(PATH)
cv2.imshow("Original logo", image)
B, G, R = cv2.split(image)
merged = cv2.merge([R, G, B])
cv2.imshow("Altered logo", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
