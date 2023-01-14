import unittest
from draw_io import parse_drawio


class TestDrawIo(unittest.TestCase):
    def test_blueprint_creation(self):
        xml_file = "draw_io/example_simple.xml"
        blueprint = parse_drawio.draw_io_xml_to_blueprint(xml_file)

        self.assertEqual(['exit', 'label_1', 'label_2', 'label_3', 'start'], blueprint.actions)
        self.assertEqual(['state_2', 'state_1', 'state_3', 'start', 'end'], blueprint.state_labels)
