import os

ROOT_PATH = "/".join(os.path.abspath(__file__).split("/")[:-2]) + "/"
DATASET_PATH = f"{ROOT_PATH}/data/photos/"
LABELS_PATH = f"{ROOT_PATH}/data/labels/"
TRAIN_DATASET_PATH = f"{ROOT_PATH}/data/train/"
TEST_DATASET_PATH = f"{ROOT_PATH}/data/test/"
ANNOTATIONS_FILE = f"{ROOT_PATH}/data/annotations.xml"
WEIGHTS_PATH = f"{ROOT_PATH}/src/runs/detect/train/weights/best.pt"

CHARS_MAP = {"1": "I", "2": "Z", "3": "C", "5": "S", "0": "O", "7": "Z"}
REV_CHARS_MAP = {"I": "1", "Z": "2", "C": "3", "S": "5", "O": "0"}
DATA_SIZE = 100
NUM_THREADS = 4
