import cv2

image = cv2.imread("../images/joe.jpg")
(height, width) = image.shape[:2]
piece_height = height // 3
piece_width = width // 3
pieces_coordinates = ()

pieces = []

for i in range(3):
    start_y = i * piece_width
    stop_y = height - 1 if i == 2 else (i + 1) * piece_width
    for j in range(3):
        start_x = j * piece_width
        stop_x = width - 1 if j == 2 else (j + 1) * piece_width
        pieces.append(((start_y, stop_y), (start_x, stop_x)))

print(pieces)

for index, piece_coordinates in enumerate(pieces):
    image_part = image[
        piece_coordinates[0][0] : piece_coordinates[0][1],
        piece_coordinates[1][0] : piece_coordinates[1][1],
    ]
    cv2.imshow(f"Joe part {index + 1}", image_part)

cv2.waitKey(0)
cv2.destroyAllWindows()
