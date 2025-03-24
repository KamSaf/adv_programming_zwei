import cv2


frame_1 = cv2.imread("../images/frame_1.png")
frame_2 = cv2.imread("../images/frame_2.png")

diff = cv2.absdiff(frame_1, frame_2)
print(diff)
cv2.imshow("Frame difference", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
