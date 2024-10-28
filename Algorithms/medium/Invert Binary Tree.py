# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def insert(self, value):
#         currentNode = self
#         while True:
#             if value < currentNode.value:
#                 if currentNode.left is not None:
#                     currentNode = currentNode.left
#                 else:
#                     currentNode.left = BST(value)
#                     break
#             elif value >= currentNode.value:
#                 if currentNode.right is not None:
#                     currentNode = currentNode.right
#                 else:
#                     currentNode.right = BST(value)
#                     break
#
#
# def BSTTraversal(tree, order="inOrder"):
#     result = []
#     if order == "inOrder":
#         inOrderTraversal(tree, result)
#     return result
#
#
# def inOrderTraversal(tree, result):
#     if tree is None:
#         return
#     inOrderTraversal(tree.left, result)
#     result.append(tree.value)
#     inOrderTraversal(tree.right, result)
#     return
#
#
# def minHeightBST(array):
#     return constructMinHeightBst(array, 0, len(array) - 1)
#
#
# def constructMinHeightBst(array, startIdx, endIdx):
#     if endIdx < startIdx:
#         return None
#     midIdx = (startIdx + endIdx) // 2
#     bst = BST(array[midIdx])
#     bst.left = constructMinHeightBst(array, startIdx, midIdx - 1)
#     bst.right = constructMinHeightBst(array, midIdx + 1, endIdx)
#     return bst


# O(n) time | O(n) space
def invertBinaryTree(tree):
    if tree is None:
        return
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    return tree


# O(n) time | O(n) space
def invertBinaryTree2(tree):
    queue = [tree]
    while queue:
        node = queue.pop(0)
        node.left, node.right = node.right, node.left
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return tree


arr = [1, 2, 5, 7, 10, 13, 14, 15, 22]
minBst = minHeightBST(arr)
print(BSTTraversal(minBst, "inOrder"))
print(BSTTraversal(invertBinaryTree(minBst), "inOrder"))

