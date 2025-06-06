import os
import random

ROOT_PATH = "/".join(os.path.abspath(__file__).split("/")[:-2]) + "/"
SEED = 98765
# SEED = 123
ANNOTATIONS_FILE = "annotations.xml"

random.seed(SEED)
