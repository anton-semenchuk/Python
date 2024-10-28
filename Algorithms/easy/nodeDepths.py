class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is not None:
                    currentNode = currentNode.left
                else:
                    currentNode.left = BST(value)
                    break
            elif value >= currentNode.value:
                if currentNode.right is not None:
                    currentNode = currentNode.right
                else:
                    currentNode.right = BST(value)
                    break


# O(n) time | O(h) space - where h is the height of the Binary Tree
def nodeDepths(tree, depth=0):
    if tree is None:
        return 0
    return depth + nodeDepths(tree.left, depth + 1) + nodeDepths(tree.right, depth + 1)


# O(n) time | O(h) space - where h is the height of the Binary Tree
def nodeDepths2(tree):
    sumOfDepths = 0
    stack = [{"node": tree, "depth": 0}]
    while stack:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sumOfDepths


bst = BST(50)
nodes = [30, 20, 40, 70, 60, 80]
for node in nodes:
    bst.insert(node)
print("NodeDepths:", nodeDepths(bst))
