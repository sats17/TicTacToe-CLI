from Backend.Board import Board
from Frontend.Player import Player


def main(player1Data, player2Data, board):
    isGameGoing = True
    whoseNextMove = "player1"
    whoWon = None
    isMatchDraw = False
    while isGameGoing:
        if whoseNextMove == "player1":
            isInvalidInput = True
            index = list(
                map(int, input("Hey " + player1Data.getPlayerName() + " enter the index numbers from board to "
                                                                      "hit the board : ").strip().split()))
            response = board.enter_move(index, player1Data.getPlayerValue())
            while isInvalidInput:
                if not response['isValidIndex']['answer'] or not response['isValidIndex']['answer']:
                    isInvalidInput = True
                    print("Oops you have entered wrong index value")
                    index = list(
                        map(int, input("Please re-enter again..").strip().split()))
                    response = board.enter_move(index, player1Data.getPlayerValue())
                else:
                    isInvalidInput = False
                    print("Backend resposne was ", response)
                    if 'isUserWin' in response:
                        isGameGoing = False
                        whoWon = player1Data
                    if 'isMatchDraw' in response:
                        isGameGoing = False
                        isMatchDraw = True
            whoseNextMove = "player2"
        else:
            isInvalidInput = True
            index = list(
                map(int, input("Hey " + player2Data.getPlayerName() + " enter the index numbers from board to "
                                                                      "hit the board : ").strip().split()))
            response = board.enter_move(index, player2Data.getPlayerValue())
            while isInvalidInput:
                if not response['isValidIndex']['answer'] or not response['isValidIndex']['answer']:
                    isInvalidInput = True
                    print("Oops you have entered wrong index value")
                    index = list(
                        map(int, input("Please re-enter again..").strip().split()))
                    response = board.enter_move(index, player2Data.getPlayerValue())
                else:
                    isInvalidInput = False
                    print("Backend response was ", response)
                    if 'isUserWin' in response:
                        isGameGoing = False
                        whoWon = player2Data
                    if 'isMatchDraw' in response:
                        isGameGoing = False
                        isMatchDraw = True
            whoseNextMove = "player1"
        print("After entering move board looks like")
        displayBoard(board.get_dashboard())
    if isMatchDraw:
        return "Hey, match is draw.. You both played well.."
    return whoWon.getPlayerName() + "Won the game"


def generateBoard(size):
    return Board(size)


def displayBoard(boardData):
    for i in boardData:
        print(i)


def preparePrerequisites():
    data = []
    name = input("Enter first player name: ")
    value = input("Pick X or O: ").lower()
    if value not in ['x', 'o']:
        print("Please enter either X or O")
        exit()
    player1 = Player(name, value)
    name = input("Enter second player name: ")
    if player1.getPlayerValue() == 'x':
        value = 'o'
    if player1.getPlayerValue() == 'o':
        value = 'y'
    player2 = Player(name, value)
    print("Players information \n", "Player 1 : ", player1.getPlayerName(), " ", player1.getPlayerValue(), "\n Player "
                                                                                                           "2 : ",
          player2.getPlayerName(), " ", player2.getPlayerValue())
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
    print("Welcome to CLI based TicTacToe game ")
    prerequisitesData = preparePrerequisites()
    boardSize = prerequisitesData[0]
    player1Data = prerequisitesData[1]
    player2Data = prerequisitesData[2]
    board = generateBoard(boardSize)
    print("Your board looks like this ")
    displayBoard(board.get_dashboard())
    response = main(player1Data, player2Data, board)
    print(response)
