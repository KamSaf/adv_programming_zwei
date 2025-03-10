import cv2

image = cv2.imread("../images/joe.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(_, max_val, _, max_loc) = cv2.minMaxLoc(gray)
print(f"Maximum value {max_val} at {max_loc}")
