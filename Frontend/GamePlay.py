from Backend.Board import Board


def main(player1Data, player2Data, board):
    isPlayerWin = False
    isMatchDraw = False
    while not isPlayerWin or not isMatchDraw:
        print(board.get_dashboard())
        isPlayerWin = True


def generateBoard(size):
    return Board(size)


def displayBoard(board):
    for i in board:
        print(i)


def preparePrerequisites():
    data = []
    player1 = dict()
    name = input("Enter first player name: ")
    value = input("Pick X or O: ").lower()
    if value not in ['x', 'o']:
        print("Please enter either X or O")
        exit()
    player1['name'] = name
    player1['value'] = value
    player2 = dict()
    name = input("Enter second player name: ")
    player2['name'] = name
    if player1.get('value') == 'x':
        player2['value'] = 'o'
    if player1.get('value') == 'o':
        player2['value'] = 'y'
    print("Players information \n", "Player 1 : ", player1.get('name'), " ", player1.get('value'), "\n Player 2 : ",
          player2.get('name'), " ", player2.get('value'))
    try:
        boardSize = int(input("Enter board size: "))
    except ValueError:
        print("That's not an number, please enter board size between 0 to 5!")
        exit()
    if boardSize <= 0 or boardSize > 5:
        print("Please enter board size between 0 to 5!")
        exit()
    data.append(boardSize)
    data.append(player1)
    data.append(player2)
    return data


if __name__ == "__main__":
    isPlayerWin = False
    isMatchDraw = False
    # print(not isPlayerWin)
    if not isPlayerWin:
        print("Yes")
    # print("Welcome to CLI based TicTacToe game ")
    # prerequisitesData = preparePrerequisites()
    # boardSize = prerequisitesData[0]
    # player1Data = prerequisitesData[1]
    # player2Data = prerequisitesData[2]
    # board = generateBoard(boardSize)
    # print("Your board looks like this ")
    # displayBoard(board.get_dashboard())
    # main(player1Data, player2Data, board)

