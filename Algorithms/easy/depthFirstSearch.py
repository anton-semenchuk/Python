class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space where v is the vertices and e is the edges
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


tree = Node("a")
tree.addChild("w")
tree.children[0].addChild("x")
arr = ["b", "c", "d", "e", "f"]
for el in arr:
    tree.addChild(el)
print(tree.depthFirstSearch([]))
