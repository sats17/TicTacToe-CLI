from tictactoe import Board


class GameFlow(Board.Board):

    def __init__(self, size):
        super().__init__(size)
        self.size = size

    def captureMove(self, index, value):
        if not isinstance(value, str) or value.lower() != 'x' or value.lower() != 'o':
            return False


a = GameFlow(3)
print(a.verticalPossibility)
print(a.dashBoard)
print(a.captureMove(1, '/'))
