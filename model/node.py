class Node:
    def __init__(self, id, parent=None):
        self.id = id
        self.parent = parent
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"
