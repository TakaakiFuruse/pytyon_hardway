import numpy as np


class Game(object):
    """docstring for Game"""

    def __init__(self):
        self.answer_list = None
        self.player_victory = False
        self.hit = None
        self.blow = None

    def generate_answer_list(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        np.random.shuffle(array)
        self.answer_list = array[0:4]
        print(self.answer_list)

    def answer_validator(self, input_list):
        def input_list_lengh_validator(input_list):
            if len(input_list) > 4 or len(input_list) < 3 :
                raise InvalidGuessError(input_list)
            elif len(np.unique(input_list)) < 4:
                raise InvalidGuessError(input_list)

        def num_validator(input_list):
            for num in input_list:
                if num not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    raise InvalidGuessError(input_list)

        def blow_validator(input_list):
            counter = 0
            for num in input_list:
                if num in self.answer_list:
                    counter += 1
            self.blow = counter

        def hit_validator(input_list):
            counter = 0
            for num in input_list:
                if num in self.answer_list and (input_list.index(num) is (self.answer_list).index(num)):
                    counter += 1
            self.hit = counter

        def victory_validator(input_list):
            if self.hit is 4:
                self.player_victory = True
                print('YOU WIN!!')

        return(input_list_lengh_validator, num_validator,
               blow_validator, hit_validator, victory_validator)

    def validation_engine(self, input_list):
        validations = Game.answer_validator(self, input_list)
        for validation in validations:
            validation(input_list)
        print("Hit: {0}, Blow: {1}".format(self.hit, self.blow))
        self.hit = 0
        self.blow = 0


class InvalidGuessError(Exception):
    """docstring for InvalidGuess"""

    def __init__(self, a_list):
        self.arg = a_list

game = Game()
game.generate_answer_list()

while game.player_victory is False:
    try:
        input_txt = input("> Guess Number:  ")
        input_list = [int(num) for num in input_txt]
        game.validation_engine(input_list)
    except InvalidGuessError:
        print("Try again, your guess was invalid.")
