import cv2

image = cv2.imread("../images/joe.jpg")
if image is None:
    print("No image found at given path")
else:
    print("Image has been loaded.")
