import cv2

image = cv2.imread("../images/jeep.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
for name, chan in zip(("H", "S", "V"), cv2.split(hsv)):
    if name == "S":
        # for r in chan:
        print(name)
        # chan = [[c + 30 for c in r] for r in chan]
    cv2.waitKey(0)
    cv2.destroyAllWindows()
