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


# O(n) time | O(n) space
def branchSums(tree):
    sums = []
    _branchSums(tree, 0, sums)
    return sums


def _branchSums(tree, currentSum, allBranchSums):
    if tree is None:
        return
    currentSum += tree.value
    if tree.left is None and tree.right is None:
        allBranchSums.append(currentSum)
        return
    _branchSums(tree.left, currentSum, allBranchSums)
    _branchSums(tree.right, currentSum, allBranchSums)


bst = BST(50)
nodes = [30, 20, 40, 70, 60, 80]
for node in nodes:
    bst.insert(node)
print("Branch sums:", branchSums(bst))
