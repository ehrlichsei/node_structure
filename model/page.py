from .node import Node

class Page(Node):
    def __init__(self, id, parent=None, properties=None):
        super().__init__(id, parent)
        self.properties = properties if properties is not None else {}

    def add_property(self, key, value):
        self.properties[key] = value