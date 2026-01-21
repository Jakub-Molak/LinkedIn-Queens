import random 
size = 8
if size < 4:
    exit("Size must be at least 4")
midPoint = (size // 2) if size % 2 != 0 else size // 2 - 1

def generateValidColumnPosition(virtualBoard,rowNo,board):
    drawBoard(board)
    print("Virtual row to Check" + str(virtualBoard[rowNo]))
    valid_positions =  [pos for pos in range(0,size) if virtualBoard[rowNo][pos] != 1]
    print("Virtual row to Check" + str(valid_positions))
    if len(valid_positions) == 0:
        breakpoint
        print("shit")
    return valid_positions[random.randint(0,len(valid_positions)-1)]

def drawBoard(board):
    [print(row, end="\n") for row in board]

def updateVirtualBoard(virtualBoard, pos):
    x = pos[0]
    y = pos[1]

    virtualBoard[y][x] = 1
    # Get the valid corners to update on virtual board
    corners = [
        [y-1,x-1] if y-1 >= 0 and x-1 >= 0 else []
        ,[y-1,x+1] if y-1 >= 0 and x+1 < size else []
        ,[y+1,x-1] if y+1 < size and x-1 >= 0 else []
        ,[y+1,x+1] if y+1 < size and x+1 < size else []
    ]
    for (corY,corX) in [_ for _ in corners if len(_)>0]:
        virtualBoard[corY][corX] = 1
    
    ## Update column
    virtualBoard[y] = [1] * size
    ## update row
    for row in range(0,size):
        virtualBoard[row][x] = 1
        
def updateBoard(board,virtualBoard,pos,queenNo):
    x = pos[0]
    y = pos[1]

    board[y][x] = queenNo
    updateVirtualBoard(virtualBoard,(x,y))

def validcardinalPosition(board,pos):
    x = pos[0]
    y = pos[1]
    cardinalPos = [
    [y,x-1] if x-1 >= 0 else []
    ,[y,x+1] if x+1 < size else []
    ,[y-1,x] if y-1 >= 0 else []
    ,[y+1,x] if y+1 < size else []
    ] # flips x and y in position
    return [_ for _ in cardinalPos if len(_) > 0] 
    

def cardinalPositionAvailable(board,pos):
    cardinalPos = validcardinalPosition(board,pos)
    availablePositions = [position for position in cardinalPos if board[position[0]][position[1]] == 0]
    print(availablePositions)
    return availablePositions

         

# This needs to be reworked so that it should randomly pick randombly from positions that have the most empty positions around it,
#  edge positions should have + 1 for theoretical extra cell
for _ in range(0,100):
    base =  [[0] * size for _ in range(size)]
    virtualBase = [[0] * size for _ in range(size)]
    rowMinPoint = midPoint - 1
    rowMaxPoint = midPoint + 1
    startX = random.randint(0, size - 1)
    updateBoard(base,virtualBase,(startX,midPoint),1) 

    boardPosition = {"1": [[startX,midPoint]]}

    ## Fill rest of board
    for queenNo in range(2,size+1):
        if queenNo % 2 == 0:
            xPos = generateValidColumnPosition(virtualBase,rowMaxPoint,base)
            boardPosition[f"{queenNo}"] = [[xPos,rowMaxPoint]]
            updateBoard(base,virtualBase,(xPos,rowMaxPoint),queenNo)
            rowMaxPoint = rowMaxPoint + 1
        else:
            xPos = generateValidColumnPosition(virtualBase,rowMinPoint,base)
            boardPosition[f"{queenNo}"] = [[xPos,rowMinPoint]]
            updateBoard(base,virtualBase,(xPos,rowMinPoint),queenNo)
            rowMinPoint = rowMinPoint - 1


# drawBoard(base)

# ## board filling
# for i in range(0,(size**2)-size):
#     availableSpots = {}
#     for _ in range(1,size+1):
#         availableSpotsByQueen = []
#         for position in  boardPosition[f"{_}"]:
#             availablePositions += availableSpotsByQueen.append(cardinalPositionAvailable(base,(position[0],position[1])))
#         # availablePositions = availableSpotsByQueen
#         print(availableSpots)
#         break
# test = cardinalPositionAvailable(base,boardPosition["1"][0])
