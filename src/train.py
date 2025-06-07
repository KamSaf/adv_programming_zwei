import random
import os
from ultralytics import YOLO
from config import ROOT_PATH, ANNOTATIONS_FILE
from utils import create_dir, copy_dataset
from label_data import convert_labels


def split_datasets(
    data_path: str,
    ds_split_ratio: float = 0.3,
    train_ds_path: str = ROOT_PATH + "data/train/",
    test_ds_path: str = ROOT_PATH + "data/test/",
) -> None:
    """
    Function splitting whole dataset into train and test sections
    and converting XML labels into .txt files.

    Parameters:
        data_path (str): path to directory with dataset

        ds_split_ratio (float): percentage of dataset which is to be assigned to testing dataset

        train_ds_path (str): path where train dataset is to be stored

        test_ds_path (str): path where testing dataset is to be stored
    """
    for dir in (train_ds_path, test_ds_path):
        create_dir(dir)
    files_list = os.listdir(data_path)
    random.shuffle(files_list)
    ds_len = len(files_list)
    split_index = int(ds_len * (1 - ds_split_ratio))
    train_ds = files_list[:split_index]
    test_ds = files_list[split_index:]
    copy_dataset(data_path, train_ds, train_ds_path)
    copy_dataset(data_path, test_ds, test_ds_path)


def train() -> None:
    """
    Function firing up model training
    """
    model = YOLO("yolo11n.pt")
    model.train(data="data.yaml", epochs=50, imgsz=640, cache=True, workers=8)


if __name__ == "__main__":
    convert_labels(ANNOTATIONS_FILE)
    split_datasets(data_path=ROOT_PATH + "data/photos/")
    train()
