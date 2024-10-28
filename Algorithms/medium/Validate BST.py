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
#     def contains(self, value):
#         currentNode = self
#         while currentNode is not None:
#             if value < currentNode.value:
#                 currentNode = currentNode.left
#             elif value > currentNode.value:
#                 currentNode = currentNode.right
#             else:
#                 return True
#         return False
#
#     def remove(self, value, parentNode=None):
#         currentNode = self
#         while currentNode is not None:
#             if value < currentNode.value:
#                 parentNode = currentNode
#                 currentNode = currentNode.left
#             elif value > currentNode.value:
#                 parentNode = currentNode
#                 currentNode = currentNode.right
#             else:
#                 if currentNode.left is not None and currentNode.right is not None:
#                     currentNode.value = currentNode.right.getMinValue()
#                     currentNode.right.remove(currentNode.value, currentNode)
#                 elif parentNode is None:
#                     if currentNode.left is not None:
#                         currentNode.value = currentNode.left.value
#                         currentNode.left = currentNode.left.left
#                         currentNode.right = currentNode.left.right
#                     elif currentNode.right is not None:
#                         currentNode.value = currentNode.right.value
#                         currentNode.left = currentNode.right.left
#                         currentNode.right = currentNode.right.right
#                     else:
#                         # This is a single-node tree; do nothing.
#                         pass
#                 elif parentNode.left == currentNode:
#                     parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
#                 elif parentNode.right == currentNode:
#                     parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
#                 break
#         return self
#
#     def getMinValue(self):
#         currentNode = self
#         while currentNode.left is not None:
#             currentNode = currentNode.left
#         return currentNode.value


# O(n) time O(d) space
def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if minValue > tree.value or maxValue <= tree.value:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)


bst = BST(5)
arr = [4, 1, 7, 6, 3, 8, 7.5, 7.6]
for num in arr:
    bst.insert(num)
print(validateBst(bst))

