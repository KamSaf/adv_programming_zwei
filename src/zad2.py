import cv2

PATH = "../images/opencv_logo.png"
image = cv2.imread(PATH)
color_names = ("Blue", "Green", "Red")
split_channels = cv2.split(image)
colors = {name: split_channels[index] for index, name in enumerate(color_names)}
for color_name, channel in colors.items():
    cv2.imshow(color_name, channel)
cv2.waitKey(0)
cv2.destroyAllWindows()
