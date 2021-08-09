from Backend.Response import Response
from Backend.TicTacToeI import TicTacToeI
import logging


class Board(TicTacToeI):
    __size = None
    __dashBoard = None
    __horizontalPossibility = None
    __verticalPossibility = None
    __crossPossibility = None

    def __init__(self, size):
        self.__size = size
        self.__dashBoard = [[0 for col in range(size)] for row in range(size)]
        self.__createHorizontalPossibility(size)
        self.__createVerticalPossibility(size)
        self.__createCrossPossibility(size)

    def get_dashboard(self):
        return self.__dashBoard

    def __createHorizontalPossibility(self, size):
        self.__horizontalPossibility = [[[0, 0] for col in range(size)] for row in range(size)]
        for i in range(0, size):
            for j in range(0, size):
                self.__horizontalPossibility[i][j] = [i, j]

    def __createVerticalPossibility(self, size):
        self.__verticalPossibility = [[[0, 0] for col in range(size)] for row in range(size)]
        for i in range(0, size):
            for j in range(0, size):
                self.__verticalPossibility[i][j] = self.__horizontalPossibility[j][i]

    def __createCrossPossibility(self, size):
        self.__crossPossibility = [[[0, 0] for col in range(size)] for row in range(2)]
        m = 0
        n = 0
        for i in range(0, size):
            self.__crossPossibility[0][i] = [m, n]
            m += 1
            n += 1
        m = 0
        n = size - 1
        for i in range(0, size):
            self.__crossPossibility[1][i] = [m, n]
            m += 1
            n -= 1

    def enter_move(self, index: list, value: str) -> object:
        response_obj = Response()
        lowerCaseValue = value.lower()
        if not isinstance(value, str) or lowerCaseValue not in self.get_values():
            logging.error("Error occurred while validating value")
            return response_obj.error(40001, "Invalid value entered, please enter o or x").build()
        if not isinstance(index, list) or len(index) != 2 or not isinstance(index[0], int) or not isinstance(index[1],
                                                                                                             int):
            logging.error("Error occurred while validating index")
            return response_obj.is_valid_index(False, "Invalid index entered").build()
        if index[0] < 0 or index[0] > self.__size - 1 or index[1] < 0 or index[1] > self.__size - 1:
            logging.error("Error occurred while validating index")
            return response_obj.is_valid_index(False, "Invalid index entered").build()
        if self.__dashBoard[index[0]][index[1]] != 0:
            logging.error("Error occurred while validating index")
            return response_obj.is_valid_index(False, "Invalid index entered").build()
        self.__dashBoard[index[0]][index[1]] = lowerCaseValue
        logging.debug("Updated dashboard is ", self.__dashBoard)
        response_obj.is_valid_value(True, None).is_valid_index(True, None)
        if self.__resultChecker(index, lowerCaseValue) == "win":
            return response_obj.is_user_win(True).build()
        if self.__drawChecker():
            return response_obj.is_match_draw(True).build()
        return response_obj.build()

    def __resultChecker(self, index, value):
        for possibilityIndex in range(len(self.__horizontalPossibility)):
            logging.debug("Horizontal possibility at ", self.__horizontalPossibility[possibilityIndex])
            if index in self.__horizontalPossibility[possibilityIndex]:
                logging.debug("Found match in horizontal possibility ", index)
                successCounter = 0
                for possibilityValues in self.__horizontalPossibility[possibilityIndex]:
                    logging.debug("Possibility values are ", possibilityValues)
                    dashBoardValue = self.__dashBoard[possibilityValues[0]][possibilityValues[1]]
                    if value == dashBoardValue:
                        successCounter += 1
                if successCounter == self.__size:
                    logging.debug("User win at horizontal possibility with index ",
                                  self.__horizontalPossibility[possibilityIndex])
                    return "win"

        for possibilityIndex in range(len(self.__verticalPossibility)):
            logging.debug("Vertical possibility at ", self.__verticalPossibility[possibilityIndex])
            if index in self.__verticalPossibility[possibilityIndex]:
                logging.debug("Found match in vertical possibility ", index)
                successCounter = 0
                for possibilityValues in self.__verticalPossibility[possibilityIndex]:
                    logging.debug("Possibility values are ", possibilityValues)
                    dashBoardValue = self.__dashBoard[possibilityValues[0]][possibilityValues[1]]
                    if value == dashBoardValue:
                        successCounter += 1
                if successCounter == self.__size:
                    logging.debug("User win at vertical possibility with index ",
                                  self.__verticalPossibility[possibilityIndex])
                    return "win"

        for possibilityIndex in range(len(self.__crossPossibility)):
            logging.debug("Cross possibility at ", self.__crossPossibility[possibilityIndex])
            if index in self.__crossPossibility[possibilityIndex]:
                logging.debug("Found match in cross possibility ", index)
                successCounter = 0
                for possibilityValues in self.__crossPossibility[possibilityIndex]:
                    logging.debug("Possibility values are ", possibilityValues)
                    dashBoardValue = self.__dashBoard[possibilityValues[0]][possibilityValues[1]]
                    if value == dashBoardValue:
                        successCounter += 1
                if successCounter == self.__size:
                    logging.debug("User win at cross possibility with index ",
                                  self.__crossPossibility[possibilityIndex])
                    return "win"

    def __drawChecker(self):
        for i in self.__dashBoard:
            if 0 in i:
                return False
        return True
