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


# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def findClosestNumber(tree, target, closest=float("inf")):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest


# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space
def findClosestNumber2(tree, target, closest=float("inf")):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestNumber(tree.left, target, closest)
    elif target > tree.value:
        return findClosestNumber(tree.right, target, closest)
    return closest


bst = BST(50)
nodes = [30, 20, 40, 70, 60, 80]
for node in nodes:
    bst.insert(node)
print("Find closest number 44:", findClosestNumber(bst, 44))
