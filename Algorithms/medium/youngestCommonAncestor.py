# every descendant in the tree have only one direct ancestor and no his own descendants
# O(d) time | O(1) space
def youngestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)


def getDescendantDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        descendant = descendant.ancestor
        depth += 1
    return depth


def backtrackAncestralTree(lesserDescendant, higherDescendant, diff):
    while diff > 0:
        lesserDescendant = lesserDescendant.ancestor
        diff -= 1
    while lesserDescendant != higherDescendant:
        lesserDescendant = lesserDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lesserDescendant
