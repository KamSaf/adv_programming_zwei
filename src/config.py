import os

ROOT_PATH = "/".join(os.path.abspath(__file__).split("/")[:-2]) + "/"
ANNOTATIONS_FILE = "annotations.xml"
CHARS_MAP = {"1": "I", "2": "Z", "3": "C", "5": "S", "0": "O", "7": "Z"}
REV_CHARS_MAP = {"I": "1", "Z": "2", "C": "3", "S": "5", "O": "0"}
DATA_SIZE = 100
NUM_THREADS = 4
