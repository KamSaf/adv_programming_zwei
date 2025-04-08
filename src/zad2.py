import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("../images/grid.jpg", cv2.IMREAD_GRAYSCALE)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
iterations_range = range(1, 20)
thickness_measurements = []

for i in iterations_range:
    dilated = cv2.dilate(binary_image, kernel, iterations=i)
    mean_thickness = np.mean(dilated.astype(np.float32))
    thickness_measurements.append(mean_thickness)
    cv2.imshow(f"dylated_iter_{i}", dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

plt.figure(figsize=(10, 5))
plt.plot(iterations_range, thickness_measurements, marker="o", color="orange")
plt.title("Zmiana grubości obiektów w zależności od liczby iteracji dylatacji")
plt.xlabel("Liczba iteracji dylatacji")
plt.ylabel("Średnia jasność pikseli (przybliżona grubość)")
plt.grid(True)
plt.show()
