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


# O(n) time | 0(n) space
def BSTTraversal(tree, order="inOrder"):
    result = []
    if order == "inOrder":
        inOrderTraversal(tree, result)
    elif order == "preOrder":
        preOrderTraversal(tree, result)
    elif order == "postOrder":
        postOrderTraversal(tree, result)
    return result


def inOrderTraversal(tree, result):
    if tree is None:
        return
    inOrderTraversal(tree.left, result)
    result.append(tree.value)
    inOrderTraversal(tree.right, result)
    return


def preOrderTraversal(tree, result):
    if tree is None:
        return
    result.append(tree.value)
    preOrderTraversal(tree.left, result)
    preOrderTraversal(tree.right, result)
    return


def postOrderTraversal(tree, result):
    if tree is None:
        return
    postOrderTraversal(tree.left, result)
    postOrderTraversal(tree.right, result)
    result.append(tree.value)
    return


bst = BST(5)
arr = [4, 1, 7, 6, 3, 8, 7.5, 7.6]
for num in arr:
    bst.insert(num)
print(BSTTraversal(bst, "inOrder"))

