from Backend.Board import Board


def main():
    board = Board(3)
    print(board.get_dashboard())
    return None


if __name__ == "__main__":
    player1 = dict()
    name = input("Enter player one name: ")
    value = input("Pick X or O: ")
    if value.lower() not in ['x', 'o']:
        print("Please enter either X or O")
        exit()
    player1['name'] = name
    player1['value'] = value.lower()
    player2 = dict()
    name = input("Enter player two name: ")
    player2['name'] = name
    if player1.get('value') == 'x':
        player2['value'] = 'o'
    if player1.get('value') == 'o':
        player2['value'] = 'y'
    print("Players information \n", "Player 1 : ", player1.get('name'), " ", player1.get('value'), "\n Player 2 : ",
          player2.get('name'), " ", player2.get('value'))
    boardSize = input("Enter board size: ") # Get int and handle error here
    if not isinstance(boardSize, int) or boardSize <= 0 or boardSize > 5:
        print("Please enter only number which is greater than 0 and less than 5")
        exit()
    main() # calling main function
