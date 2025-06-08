import xml.etree.ElementTree as ET
from config import ROOT_PATH, ANNOTATIONS_FILE
from utils import norm_coord, norm_size, create_dir, purge_dir


def parse_xml(xml_path: str) -> dict[str, tuple[float, float, float, float]]:
    """
    Function converting XML format labels to dictonary.

    Parameters:
        xml_path (str): path to .xml file containing labels

    Returns:
        labels (dict[str, tuple[float, float, float]]):
        dictonary with file name as key and YOLO format label as value
    """
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
        labels[f"{image.attrib['name'].split('.')[0]}.txt"] = (
            norm_coord(xtl, xbr, width),
            norm_coord(ytl, ybr, height),
            norm_size(xtl, xbr, width),
            norm_size(ytl, ybr, height),
        )
    return labels


def convert_labels(xml_path: str, output_dir: str = ROOT_PATH + "data/labels/") -> None:
    """
    Function converting XML labels to YOLO style labels and saving them to separate .txt files.

    Parameters:
        xml_file (str): path to .xml file with labels

        output_dir (str): path to directory where labels are supposed to be saved in
    """
    labels = parse_xml(xml_path)
    purge_dir(output_dir)
    create_dir(output_dir)
    for f_name, label in labels.items():
        with open(output_dir + f_name, "w") as f:
            f.write(" ".join(["0"] + list(map(str, label))))


if __name__ == "__main__":
    annotations_path = f"{ROOT_PATH}data/{ANNOTATIONS_FILE}"
    convert_labels(annotations_path)
