import numpy as np


class Game(object):
    """docstring for Game"""

    def __init__(self):
        self.answer_list = None
        self.player_victory = False

    def generate_answer_list(self):
        array = np.arange(10)
        np.random.shuffle(array)
        self.answer_list = array[0:4]
        print(self.answer_list)

    def answer_validator(self, input_list):
        hit = 0
        blow = 0

        def input_list_lengh_validator(input_list):
            if len(input_list) not in np.arange(len(self.answer_list)):
                raise InvalidGuessError()

        def num_validator(input_list):
            for num in input_list:
                if num not in np.arange(10):
                    raise InvalidGuessError()

        def blow_validator(input_list):
            blow = [1 for num in input_list if num in self.answer_list]
            return np.sum(blow)

        def hit_validator(input_list):
            hit = [1 for num in input_list
                   if num in self.answer_list and
                   input_list.index(num) is self.answer_list.index(num)]
            return np.sum(hit)

        def victory_validator(input_list):
            if input_list is self.answer_list:
                return True

        def result_printer():
            print("Hit: {0}, Blow: {1}".format(hit, blow))

        return(input_list_lengh_validator, num_validator,
               blow_validator, hit_validator, victory_validator, result_printer)

    def validation_engine(self, input_list):
        validations = Game.answer_validator(self, input_list)
        for validation in validations:
            print(validation(input_list))


class InvalidGuessError(Exception):
    """docstring for InvalidGuess"""

    def __init__(self, array):
        self.arg = array

game = Game()
game.generate_answer_list()

while game.player_victory is False:
    try:
        input_txt = input("> Guess Number:  ")
        input_list = list(input_txt)
        game.validation_engine(input_list)
    except InvalidGuessError:
        print("Try again, your guess was invalid.")
