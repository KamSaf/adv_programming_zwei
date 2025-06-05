import os
from shutil import copyfile
from config import ROOT_PATH


def create_dir(directory: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)


def norm_size(c1: str, c2: str, dim: str) -> float:
    f_c1, f_c2, f_dim = map(float, (c1, c2, dim))
    return (f_c2 - f_c1) / f_dim


def norm_coord(c1: str, c2: str, dim: str) -> float:
    f_c1, f_c2, f_dim = map(float, (c1, c2, dim))
    return ((f_c2 + f_c1) / 2) / f_dim


def copy_file(src: str, dest: str) -> None:
    dir = "/".join(dest.split("/")[:-1])
    create_dir(dir)
    copyfile(src, dest)


def purge_dir(path: str) -> None:
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


def copy_dataset(
    src: str,
    file_names: list[str],
    dest: str,
    labels_path: str = ROOT_PATH + "/data/labels/",
) -> None:
    purge_dir(dest)
    for file_n in file_names:
        copy_file(src + file_n, dest + file_n)
        label_name = file_n[:-3] + "txt"
        copy_file(labels_path + label_name, dest + label_name)
