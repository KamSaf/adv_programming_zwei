import sys
import cv2


params = {"start_x": 0, "stop_x": 0, "start_y": 0, "stop_y": 0}
for key in params.keys():
    try:
        params[key] = int(input(f"Enter {key.replace('_', ' ')} parameter (int):\n"))
    except Exception:
        print(f"Invalid {key.replace('_', ' ')} parameter entered.\n")
        sys.exit()

image = cv2.imread("../images/joe.jpg")

try:
    roi = image[
        params["start_y"] : params["stop_y"], params["start_x"] : params["stop_x"]
    ]
except Exception:
    print("propably wrong parameters entered, your fault not mine")
    sys.exit()

cv2.imshow("Joe Part", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
