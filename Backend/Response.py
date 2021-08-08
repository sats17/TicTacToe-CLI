class Response:
    __response = None
    __message = None
    __code = None
    __type = None
    __Error = None

    def __init__(self):
        self.__response = dict()

    def error(self, code: int, message: str):
        self.__response['response'] = {
            'code': code,
            'message': message
        }
        return self

    def is_valid_value(self, answer: bool, reason: str):
        if reason is None:
            self.__response['isValidValue'] = {
                'answer': answer
            }
        else:
            self.__response['isValidValue'] = {
                'answer': answer,
                'reason': reason
            }
        return self

    def is_valid_index(self, answer: bool, reason: str):
        if reason is None:
            self.__response['isValidIndex'] = {
                'answer': answer
            }
        else:
            self.__response['isValidIndex'] = {
                'answer': answer,
                'reason': reason
            }
        return self

    def is_user_win(self, answer: bool):
        self.__response['isUserWin'] = {
            'answer': answer
        }
        return self

    def is_match_draw(self, answer: bool):
        self.__response['isMatchDraw'] = {
            'answer': answer
        }
        return self

    def build(self):
        return self.__response
