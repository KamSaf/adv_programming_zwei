import os


def create_dir(directory: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)


def norm_size(c1: str, c2: str, dim: str) -> float:
    f_c1, f_c2, f_dim = map(float, (c1, c2, dim))
    return (f_c2 - f_c1) / f_dim


def norm_coord(c1: str, c2: str, dim: str) -> float:
    f_c1, f_c2, f_dim = map(float, (c1, c2, dim))
    return ((f_c2 + f_c1) / 2) / f_dim
