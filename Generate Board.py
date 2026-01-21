import random 
size = 5
if size < 4:
    exit("Size must be at least 4")

base =  [[0] * size for _ in range(size)]
virtualBase = [[0] * size for _ in range(size)]




def drawBoard(board):
    [print(row, end="\n") for row in board]

def updateVirtualBoard(virtualBoard, pos):
    x = pos[0]
    y = pos[1]

    virtualBoard[y][x] = 1


# def possiblePositions(board, row):


midPoint = (size // 2) if size % 2 != 0 else size // 2 - 1
randomNum = random.randint(0, size - 1)

rowMinPoint = midPoint - 1
rowMaxPoint = midPoint + 1

queensSet = 1



# while rowMinPoint >= 0:
#     if queensSet % 2 != 0:

#         base[rowMinPoint][randomNum] = 1
#         rowMinPoint -= 1



base[midPoint][randomNum] = 1
updateVirtualBoard(virtualBase, (randomNum, midPoint))
drawBoard(virtualBase)
print("")
drawBoard(base)
