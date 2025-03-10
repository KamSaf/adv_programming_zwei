import cv2
from screeninfo import get_monitors

monitor = get_monitors()[0]
screen_size = (monitor.width, monitor.height)
image = cv2.imread("../images/high_res.jpg")
image_size = image.shape[:3]
window_size = (
    screen_size[0] if image_size[0] > screen_size[0] else image_size[0],
    screen_size[1] if image_size[1] > screen_size[1] else image_size[1],
)
print(window_size)
cv2.namedWindow("Joe", cv2.WINDOW_NORMAL)
cv2.imshow("Joe", image)
cv2.resizeWindow("Joe", window_size[0], window_size[1])
cv2.waitKey(0)
cv2.destroyAllWindows()
