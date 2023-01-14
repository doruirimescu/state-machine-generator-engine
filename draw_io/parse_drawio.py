import xml.etree.ElementTree as ET
from typing import List, Tuple, Dict, Optional
from dataclasses import dataclass
"""Parse draw.io generated xml to state machine. Rectangles, arrows and recognizes substates.
"""

@dataclass
class Rectangle:
    x: int
    y: int
    width: int
    height: int
    label: str
    tooltip: str
    substates: Optional[List]

@dataclass
class Arrow:
    source: str
    target: str
    label: str

def __parse_diagram(xml_file) -> Tuple[Dict, Dict, Dict]:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    diagram = root.find("diagram")
    mxGraphModel = diagram.find("mxGraphModel")
    root = mxGraphModel.find("root")
    rectangles: Dict[str, Rectangle] = {}
    arrows: Dict[str, Arrow] = {}
    arrow_to_rectangles = {}

    # Parse Rectangles
    for child in root:
        # Parse rectangles with Tooltip
        if child.tag == "UserObject" and child.find("mxCell").attrib.get("vertex") == "1":
            id = child.attrib["id"]
            label = child.attrib["label"]
            geometry = child.find("mxCell").find("mxGeometry")
            x = geometry.attrib["x"]
            y = geometry.attrib["y"]
            width =  geometry.attrib["width"]
            height = geometry.attrib["height"]
            tooltip = child.attrib["tooltip"]
            rectangles[id] = Rectangle(x, y, width, height, label, tooltip, None)

        # Parse rectangles no Tooltip
        if child.attrib.get("vertex") == "1":
            id = child.attrib["id"]
            x = child.find("mxGeometry").attrib["x"]
            y = child.find("mxGeometry").attrib["y"]
            width = child.find("mxGeometry").attrib["width"]
            height = child.find("mxGeometry").attrib["height"]
            label = child.attrib["value"]
            rectangles[id] = Rectangle(x, y, width, height, label, None, None)
    # Parse arrows
    for child in root:
        try:
            if child.tag == "UserObject" and child.find("mxCell").find("mxGeometry").attrib.get("relative") :
                id = child.attrib["id"]
                label = child.attrib["label"]
                source = child.find("mxCell").attrib["source"]
                target = child.find("mxCell").attrib["target"]
                arrows[id] = Arrow(source, target, label)
                arrow_to_rectangles[id]={"source_rectangle" : source, "target_rectangle" : target}
            elif child.attrib.get("edge") == "1":
                id = child.attrib["id"]
                source = child.attrib["source"]
                target = child.attrib["target"]
                label = child.attrib["value"]
                arrows[id] = Arrow(source, target, label)
                arrow_to_rectangles[id]={"source_rectangle" : source, "target_rectangle" : target}
        except KeyError as e:
            error = e.args[0]
            print("KeyError", e)
            if error == "target":
                print("Make sure all arrows have a target rectangle")
            elif error == "source":
                print("Make sure all arrows have a source rectangle")
            elif error == "label":
                print("Make sure all arrows have a label")
            exit(0)
    return rectangles, arrows, arrow_to_rectangles


def find_substates(rectangles):
    for id, rectangle in rectangles.items():
        substates = []
        for id2, rectangle2 in rectangles.items():
            if id != id2:
                if float(rectangle2.x) > float(rectangle.x) and float(rectangle2.y) > float(rectangle.y) and float(rectangle2.x) + float(rectangle2.width) < float(rectangle.x) + float(rectangle.width) and float(rectangle2.y) + float(rectangle2.height) < float(rectangle.y) + float(rectangle.height):
                    substates.append(id2)
        rectangle.substates = substates


def extract_output(text: str) -> str:
    if text is None:
        return None
    start = "output:"
    end = "on_entry:"
    return text[text.find(start) + len(start): text.rfind(end)].strip()


def extract_on_entry(text: str) -> str:
    if text is None:
        return None
    start = "on_entry:"
    end = "on_exit:"
    return text[text.find(start) + len(start): text.rfind(end)].strip()


def extract_on_exit(text: str) -> str:
    if text is None:
        return None
    start = "on_exit:"
    return text[text.find(start) + len(start): -1].strip()


def print_rectangles(rectangles):
    for id, rectangle in rectangles.items():
        print("Rectangle ID: ", id)
        print("x: ", rectangle.x, "y: ", rectangle.y, "width: ", rectangle.width,
              "height: ", rectangle.height, "label: ", rectangle.label, "tooltip: ",
              rectangle.tooltip)
        if rectangle.substates:
            print("Substates: ", rectangle.substates)
        print()


def print_arrows(arrows, arrow_to_rectangles, rectangles):
    for arrow in arrows:
        arrow_entry = arrows[arrow]
        print("Arrow ID: ", arrow, "Label: ", arrow_entry.label)
        print("Source rectangle: ", rectangles[arrow_entry.source])
        print("Target rectangle: ", rectangles[arrow_entry.target])
        if arrow in arrow_to_rectangles:
            print("Start rectangle: ", arrow_to_rectangles[arrow]["source_rectangle"])
            print("End rectangle: ", arrow_to_rectangles[arrow]["target_rectangle"])
        print()


def create_blueprint(rectangles, arrows, arrow_to_rectangles):
    from state import State
    from blueprint import Blueprint

    state_labels = [rectangle.label for rectangle in rectangles.values()]
    state_outputs = [extract_output(rectangle.tooltip) for rectangle in rectangles.values()]
    action_labels = [arrows[arrow].label for arrow in arrows]

    state_list = []
    index = 1
    for rectangle_id in rectangles:
        successors = dict()
        for arrow_to_rectangle in arrow_to_rectangles:
            source_rectangle_id = arrow_to_rectangles[arrow_to_rectangle]['source_rectangle']
            target_rectangle_id = arrow_to_rectangles[arrow_to_rectangle]['target_rectangle']
            if rectangle_id == source_rectangle_id:
                arrow_label = arrows[arrow_to_rectangle].label
                successors[arrow_label] = target_rectangle_id
        rectangle_tooltip = rectangles[rectangle_id].tooltip
        state_output = extract_output(rectangle_tooltip)
        state_on_entry = extract_on_entry(rectangle_tooltip)
        state_on_exit = extract_on_exit(rectangle_tooltip)
        s = State(rectangle_id, rectangles[rectangle_id].label, successors, state_output, state_on_entry, state_on_exit)
        state_list.append(s)
        index += 1
    return Blueprint(state_labels, state_list, state_outputs, action_labels)

def draw_io_xml_to_blueprint(xml_file):
    rectangles, arrows, arrow_to_rectangles = __parse_diagram(xml_file)
    bp = create_blueprint(rectangles, arrows, arrow_to_rectangles)
    return bp
