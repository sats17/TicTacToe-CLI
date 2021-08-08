class Player:
    __name = None
    __value = None

    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    def getPlayerName(self):
        return self.__name

    def getPlayerValue(self):
        return self.__value

    def setPlayerName(self, name):
        self.__name = name

    def setPlayerValue(self, value):
        self.__value = value
