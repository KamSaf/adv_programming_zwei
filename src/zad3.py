import cv2


gray = cv2.imread("../images/noise.png", cv2.IMREAD_GRAYSCALE)

for diameter, sigmaColor, sigmaSpace in [
    (11, 21, 7),
    (11, 41, 21),
    (11, 61, 39),
    (11, 81, 49),
    (11, 101, 59),
    (11, 121, 69),
    (11, 141, 79),
    (11, 161, 89),
    (11, 181, 99),
]:
    b_blur = cv2.bilateralFilter(gray, diameter, sigmaColor, sigmaSpace)
    cv2.imshow(
        f"Bilateral filter kernel - ({diameter, sigmaColor, sigmaSpace})", b_blur
    )
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Ta metoda skutecznie redukuje szum
# Ta metoda najlepiej zachowuje krawędzie
# Najlepsze rezultaty dają parametry: (11, 101, 59)
