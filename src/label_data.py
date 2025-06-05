import os
import xml.etree.ElementTree as ET

ROOT_PATH = "/".join(os.path.abspath(__file__).split("/")[:-2])


def create_dir(directory: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)


def norm_size(c1: str, c2: str, dim: str) -> float:
    f_c1, f_c2, f_dim = map(float, (c1, c2, dim))
    return (f_c2 - f_c1) / f_dim


def norm_coord(c1: str, c2: str, dim: str) -> float:
    f_c1, f_c2, f_dim = map(float, (c1, c2, dim))
    return ((f_c2 + f_c1) / 2) / f_dim


def parse_xml(xml_path: str) -> None:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    labels = {}
    for image in root:
        if image.tag != "image":
            continue
        xtl = image.find("box").attrib["xtl"]
        ytl = image.find("box").attrib["ytl"]
        xbr = image.find("box").attrib["xbr"]
        ybr = image.find("box").attrib["ybr"]
        width = image.attrib["width"]
        height = image.attrib["height"]
        labels[f"{image.attrib['name'].split('.')[0]}.txt"] = [
            norm_coord(xtl, xbr, width),
            norm_coord(ytl, ybr, height),
            norm_size(xtl, xbr, width),
            norm_size(ytl, ybr, height),
        ]
    return labels


def convert_labels(
    xml_path: str, output_dir: str = ROOT_PATH + "/data/labels/"
) -> None:
    labels = parse_xml(xml_path)
    create_dir(output_dir)
    for f_name, label in labels.items():
        with open(output_dir + f_name, "w") as f:
            f.write(", ".join(["0"] + list(map(str, label))))


if __name__ == "__main__":
    xml_file_name = "annotations.xml"
    annotations_path = f"{ROOT_PATH}/data/{xml_file_name}"
    convert_labels(annotations_path)
