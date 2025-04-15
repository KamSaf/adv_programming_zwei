import cv2
import numpy as np


def add_gaussian_noise(image, mean=0, std=25):
    noise = np.random.normal(mean, std, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image


def blur(image):
    for kernel in [(7, 7), (10, 10), (20, 20)]:
        blur = cv2.blur(image, kernel)
        cv2.imshow("Blur", blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    for kernel in [(3, 3), (9, 9), (15, 15)]:
        gaussian_blur = cv2.GaussianBlur(image, kernel, 0)
        cv2.imshow("Gaussian blur", gaussian_blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    for k in (3, 9, 15):
        median_blur = cv2.medianBlur(image, k)
        cv2.imshow("Median blur", median_blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    for diameter, sigmaColor, sigmaSpace in [(11, 21, 7), (11, 41, 21), (11, 61, 39)]:
        b_blur = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
        cv2.imshow("Bilateral filter", b_blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


image = cv2.imread("../images/joe.jpg")
noisy_image = add_gaussian_noise(image)
cv2.imshow("noisy joe", noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
blur(noisy_image)


# najlepiej usuwa cv2.bilinearFilter
