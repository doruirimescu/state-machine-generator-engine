import xml.etree.ElementTree as ET

"""Parse draw.io generated xml to state machine. Rectangles, arrows and recognizes substates.
"""

def parse_diagram(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    diagram = root.find("diagram")
    mxGraphModel = diagram.find("mxGraphModel")
    root = mxGraphModel.find("root")
    rectangles = {}
    arrows = []
    arrow_to_rectangles = {}
    for child in root:
        if child.attrib.get("vertex") == "1":
            id = child.attrib["id"]
            x = child.find("mxGeometry").attrib["x"]
            y = child.find("mxGeometry").attrib["y"]
            width = child.find("mxGeometry").attrib["width"]
            height = child.find("mxGeometry").attrib["height"]
            label = child.attrib["value"]
            rectangles[id] = {"x": x, "y": y, "width": width, "height": height, "label": label}
    for child in root:
        if child.attrib.get("edge") == "1" and child.attrib.get("value"):
            id = child.attrib["id"]
            source = child.attrib["source"]
            target = child.attrib["target"]
            label = child.attrib["value"]
            arrows.append({"id":id,"source": source, "target": target, "label": label})
            arrow_to_rectangles[id]={"start_rectangle":source,"end_rectangle":target}
    return rectangles, arrows, arrow_to_rectangles

def find_substates(rectangles):
    for id, rectangle in rectangles.items():
        substates = []
        for id2, rectangle2 in rectangles.items():
            if id != id2:
                if float(rectangle2["x"]) > float(rectangle["x"]) and float(rectangle2["y"]) > float(rectangle["y"]) and float(rectangle2["x"]) + float(rectangle2["width"]) < float(rectangle["x"]) + float(rectangle["width"]) and float(rectangle2["y"]) + float(rectangle2["height"]) < float(rectangle["y"]) + float(rectangle["height"]):
                    substates.append(id2)
        rectangle["substates"] = substates


def print_rectangles(rectangles):
    for id, rectangle in rectangles.items():
        print("Rectangle ID: ", id)
        print("x: ", rectangle["x"], "y: ", rectangle["y"], "width: ", rectangle["width"], "height: ", rectangle["height"], "label: ", rectangle["label"])
        if "substates" in rectangle:
            print("Substates: ", rectangle["substates"])
        print()


def print_arrows(arrows, arrow_to_rectangles, rectangles):
    for arrow in arrows:
        print("Arrow ID: ", arrow["id"], "Label: ", arrow["label"])
        print("Source rectangle: ", rectangles[arrow["source"]])
        print("Target rectangle: ", rectangles[arrow["target"]])
        if arrow["id"] in arrow_to_rectangles:
            print("Start rectangle: ", arrow_to_rectangles[arrow["id"]]["start_rectangle"])
            print("End rectangle: ", arrow_to_rectangles[arrow["id"]]["end_rectangle"])
        print()


xml_file = "example.xml"
rectangles, arrows, arrow_to_rectangles = parse_diagram(xml_file)
find_substates(rectangles)
find_substates(rectangles)
print_rectangles(rectangles)
print_arrows(arrows, arrow_to_rectangles, rectangles)
xml_file = "example.xml"
rectangles, arrows, arrow_to_rectangles = parse_diagram(xml_file)
print("Arrows: ", arrows)
print("arrow_to_rectangles: ", arrow_to_rectangles)
