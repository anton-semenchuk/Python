class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))

    # O(v + e) time | O(v) space/ where v - vertices, e - edges
    def breadthFirstSearch(self, array):
        cache = [self]
        while cache:
            current = cache.pop(0)
            array.append(current.name)
            for child in current.children:
                cache.append(child)
        return array


graph = Node('Start')
arr = ['1', '2', '5', '7', '10', '13', '14', '15', '22']
for el in arr:
    graph.addChild(el)
print(graph.breadthFirstSearch([]))