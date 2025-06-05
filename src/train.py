import random
import os
from config import ROOT_PATH, SEED
from utils import create_dir, copy_dataset


def split_datasets(
    data_path: str,
    ds_split_ratio: float = 0.3,
    train_ds_path: str = ROOT_PATH + "/data/train/",
    test_ds_path: str = ROOT_PATH + "/data/test/",
) -> None:
    for dir in (train_ds_path, test_ds_path):
        create_dir(dir)
    random.seed(SEED)
    files_list = os.listdir(data_path)
    random.shuffle(files_list)
    ds_len = len(files_list)
    split_index = int(ds_len * (1 - ds_split_ratio))
    train_ds = files_list[:split_index]
    test_ds = files_list[split_index:]
    copy_dataset(data_path, train_ds, train_ds_path)
    copy_dataset(data_path, test_ds, test_ds_path)


if __name__ == "__main__":
    split_datasets(ROOT_PATH + "/data/photos/")
