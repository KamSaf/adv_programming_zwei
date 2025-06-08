import threading
import timeit
from cv2.typing import MatLike
from config import ROOT_PATH, ANNOTATIONS_FILE, DATA_SIZE, NUM_THREADS
from ocr import read_plate
from utils import evaluate, get_plate_data


def calculate_final_grade(accuracy_percent: float, processing_time_sec: float) -> float:
    """
    Calculates the final grade based on license plate OCR accuracy and processing time.
    Parameters:
    - accuracy_percent: OCR accuracy as a percentage (0–100)
    - processing_time_sec: total time to process 100 images in seconds
    Returns:
    - Grade on a scale from 2.0 to 5.0 (rounded to the nearest 0.5)
    """
    if accuracy_percent < 60 or processing_time_sec > 60:
        return 2.0
    accuracy_norm = (accuracy_percent - 60) / 40
    time_norm = (60 - processing_time_sec) / 50
    score = 0.7 * accuracy_norm + 0.3 * time_norm
    grade = 2.0 + 3.0 * score
    print(grade)
    return round(grade * 2) / 2


def run(data: list[MatLike], verbose: bool = False) -> int:
    """
    Function firing up detection and OCR on list of images
    and counting number of good readings.

    Parameters:
        data (list[MatLike]): list of images to be processed

        verbose (bool): if set to true recognised plates will be printed

    Returns:
        result (int): number of good results
    """
    good = 0
    for img, num in data:
        ocr_res = read_plate(img)
        if not ocr_res:
            continue
        match = evaluate(num, ocr_res)
        if verbose:
            print(num, ocr_res, match)
        if match:
            good += 1
    return good


def worker(subdata: list[MatLike], results: list[int]) -> None:
    """
    Function starting multithreading worker.

    Parameters:
        subdata (list[MatLike]): subset of list of images to process

        resutls (list[int]): reference to list of worker results
    """
    results.append(run(subdata, False))


if __name__ == "__main__":
    data = get_plate_data(f"{ROOT_PATH}data/{ANNOTATIONS_FILE}", DATA_SIZE)
    chunk_size = len(data) // NUM_THREADS
    threads = []
    results = []
    s = timeit.default_timer()

    for i in range(NUM_THREADS):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != NUM_THREADS - 1 else len(data)
        thread = threading.Thread(target=worker, args=(data[start:end], results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    e = timeit.default_timer()
    time_exec = e - s
    acc = sum(results) / DATA_SIZE

    print(f"accuracy: {acc * 100:.2f}%")
    print(f"exec time: {time_exec:.2f}s")
    print(f"grade: {calculate_final_grade(acc * 100, time_exec)}")
