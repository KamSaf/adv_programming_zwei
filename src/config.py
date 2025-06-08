import os
import random

ROOT_PATH = "/".join(os.path.abspath(__file__).split("/")[:-2]) + "/"
# SEED = 9865
# SEED = 123  # (seed do in)
SEED = 98765  # (seed do ==)
ANNOTATIONS_FILE = "annotations.xml"
CHARS_MAP = {"1": "I", "2": "Z", "3": "C", "5": "S", "0": "O", "7": "Z"}
REV_CHARS_MAP = {"I": "1", "Z": "2", "C": "3", "S": "5", "O": "0"}


random.seed(SEED)
