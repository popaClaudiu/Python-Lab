matrix = [
    ['f','i','r','s'],
    ['n','_','l','t'],
    ['o','b','a','_'],
    ['h','t','y','p']
]

def spiral(matrix):
    if len(matrix) == 0:
        print("The matrix is empty.")

    arr = []
    rowBegin = 0
    rowEnd = len(matrix) - 1
    columnBegin = 0
    columnEnd = len(matrix[0]) - 1

    while(rowBegin <= rowEnd and columnBegin <= columnEnd):
        for i in range(columnBegin, columnEnd + 1): # left to right
            arr.extend(matrix[rowBegin][i])
        rowBegin += 1

        for i in range(rowBegin, rowEnd + 1): # top to bottom
            arr.extend(matrix[i][columnEnd])
        columnEnd -= 1

        for i in range(columnEnd, columnBegin - 1, -1): # right to left
            arr.extend(matrix[rowEnd][i])
        rowEnd -= 1

        for i in range(rowEnd, rowBegin - 1, -1): # bottom to top
            arr.append(matrix[i][columnBegin])
        columnBegin += 1

    return "".join(arr)

print(spiral(matrix))