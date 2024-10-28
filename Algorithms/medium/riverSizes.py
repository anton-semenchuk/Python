# 0 - land, 1 - river. function should return an array of all the sizes of the rivers contained in the matrix
# The river can only be adjacent vertically or horizontally
# O(n) / O(n) time, the same space - where n is the total number of the elements in the matrix
def riverSizes(matrix):
    visited = [[False for el in matrix[0]] for row in matrix]
    sizes = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0 or visited[row][col]:
                continue
            riverSize = traverseNode(matrix, visited, row, col)
            sizes.append(riverSize)
    return sizes


def traverseNode(matrix, visited, row, col, currentSize=0):
    visited[row][col] = True
    if row + 1 < len(matrix) and matrix[row + 1][col] == 1 and not visited[row + 1][col]:
        currentSize += traverseNode(matrix, visited, row + 1, col, currentSize)
    if col + 1 < len(matrix[0]) and matrix[row][col + 1] == 1 and not visited[row][col + 1]:
        currentSize += traverseNode(matrix, visited, row, col + 1, currentSize)
    if row - 1 > 0 and matrix[row - 1][col] == 1 and not visited[row - 1][col]:
        currentSize += traverseNode(matrix, visited, row - 1, col, currentSize)
    if col - 1 > 0 and matrix[row][col - 1] == 1 and not visited[row][col - 1]:
        currentSize += traverseNode(matrix, visited, row, col - 1, currentSize)
    return currentSize + 1


# O(n) / O(n) time, the same space - where n is the total number of the elements in the matrix
def riverSizes1(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            elif matrix[i][j] == 0:
                continue
            traverseNode1(i, j, matrix, visited, sizes)
    return sizes


def traverseNode1(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodeToExplore = [[i, j]]
    while nodeToExplore:
        currentNode = nodeToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodeToExplore.append(neighbor)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i < len(matrix) - 1 and not visited[i + 1][j] and matrix[i + 1][j] == 1:
        unvisitedNeighbors.append([i + 1, j])
    if j < len(matrix[i]) - 1 and not visited[i][j + 1] and matrix[i][j + 1] == 1:
        unvisitedNeighbors.append([i, j + 1])
    if i > 0 and not visited[i - 1][j] and matrix[i - 1][j] == 1:
        unvisitedNeighbors.append([i - 1, j])
    if j > 0 and not visited[i][j - 1] and matrix[i][j - 1] == 1:
        unvisitedNeighbors.append([i, j - 1])
    return unvisitedNeighbors


landscape = [[1, 0, 0, 1, 0],
             [1, 0, 1, 0, 0],
             [0, 0, 1, 0, 1],
             [1, 0, 1, 0, 1],
             [1, 0, 1, 1, 0]]
print(riverSizes(landscape))
