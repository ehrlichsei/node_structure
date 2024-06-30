from .node import Node

class Block(Node):
    def __init__(self, id, parent=None, content=None):
        super().__init__(id, parent)
        self.content = content

    def set_content(self, content):
        self.content = content