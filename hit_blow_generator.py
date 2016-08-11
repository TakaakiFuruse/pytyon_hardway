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

    def array_validator(input_list):
        def lengh_validator(input_list):
            if len(input_list) is 4:
                return True
            else:
                return False

        def uniqunes_validator(input_list):
            if len(input_list) is len(set(input_list)):
                return True
            else:
                return False

        def num_validator(input_list):
            for num in input_list:
                if num in list(range(10)):
                    return True
                else:
                    return False

        return [lengh_validator, uniqunes_validator, num_validator]

    def answer_validator(self, input_list):
        answer_list = self.answer_list

        def blow_validator(input_list):
            counter = 0
            for num in input_list:
                if num in answer_list:
                    if (input_list.index(num) is not (answer_list).index(num)):
                        counter += 1
            self.blow = counter

        def hit_validator(input_list):
            counter = 0
            for num in input_list:
                if (input_list.index(num) is (answer_list).index(num)):
                    counter += 1
            self.hit = counter

        def victory_validator(input_list):
            if self.hit is 4:
                self.player_victory = True
                print('YOU WIN!!')

        return(blow_validator, hit_validator, victory_validator)

    def validation_engine(self, input_list):
        for validation in Game.array_validator(input_list):
            if validation(input_list) is False:
                raise InvalidGuessError(input_list)

        for validation in Game.answer_validator(self, input_list):
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
