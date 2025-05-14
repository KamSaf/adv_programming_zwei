from math import inf
import cv2
import imutils


image = cv2.imread("../images/brick.png")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(resized, 140, 255, cv2.THRESH_BINARY)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = imutils.grab_contours(cnts)
brick_count = 0
max_brick_size = (0, 0)
min_brick_size = (inf, inf)
sum_brick_height = 0
sum_brick_width = 0

for c in cnts:
    c = (c.astype("float32") * ratio).astype("int32")
    _, _, w, h = cv2.boundingRect(c)
    brick_count += 1
    if w * h > max_brick_size[0] * max_brick_size[1]:
        max_brick_size = (w, h)
    if w * h < max_brick_size[0] * max_brick_size[1]:
        min_brick_size = (w, h)
    sum_brick_height += h
    sum_brick_width += w

avg_brick_height = sum_brick_height / brick_count
avg_brick_width = sum_brick_height / brick_count

output = [
    f"Brick count: {brick_count}",
    f"\nMax brick size: {max_brick_size}",
    f"\nMin brick size: {min_brick_size}",
    f"\nAverage brick height: {avg_brick_height}",
    f"\nAverage brick width: {avg_brick_width}",
]
print("".join(output))
