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


# O(n) time | O(n) space
def minHeightBST(array):
    return constructMinHeightBst(array, 0, len(array) - 1)


def constructMinHeightBst(array, startIdx, endIdx):
    if endIdx < startIdx:
        return None
    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])
    bst.left = constructMinHeightBst(array, startIdx, midIdx - 1)
    bst.right = constructMinHeightBst(array, midIdx + 1, endIdx)
    return bst


arr = [1, 2, 5, 7, 10, 13, 14, 15, 22]
minBst = minHeightBST(arr)
print(BSTTraversal(minBst))

