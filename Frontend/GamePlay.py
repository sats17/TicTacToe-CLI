from Backend.Board import Board


def main():
    board = Board(3)
    print(board.get_dashboard())
    return None


if __name__ == "__main__":
    # Change user to player
    user1 = dict()
    name = input("Enter user one name: ")
    value = input("Pick X or O: ")
    if value.lower() not in ['x', 'o']:
        print("Please enter either X or O")
        exit()
    user1['name'] = name
    user1['value'] = value.lower()
    user2 = dict()
    name = input("Enter user two name: ")
    user2['name'] = name
    if user1.get('value') == 'x':
        user2['value'] = 'o'
    if user1.get('value') == 'o':
        user2['value'] = 'y'
    print("Users information \n", "User 1 : ", user1.get('name'), " ", user1.get('value'), "\n User 2 : ",
          user2.get('name'), " ", user2.get('value'))
    boardSize = input("Enter board size: ") # Get int and handle error here
    if not isinstance(boardSize, int) or boardSize <= 0 or boardSize > 5:
        print("Please enter only number which is greater than 0 and less than 5")
        exit()
    main()
