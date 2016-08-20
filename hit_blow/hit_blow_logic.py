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

    def array_validator(input_txt):
        assert len(input_txt) is 4, 'Too many numbers.'
        assert len(input_txt) is len(set(input_txt)), 'Num duplicated.'
        for letter in input_txt:
            assert letter.isdigit() is True, 'Not num.'

    def answer_validator(self, input_list):
        answer_list = self.answer_list

        def blow_validator(input_list):
            counter = 0
            for num in input_list:
                if num in answer_list and \
                        (input_list.index(num) is not
                         (answer_list).index(num)):
                    counter += 1
            self.blow = counter

        def hit_validator(input_list):
            counter = 0
            for num in input_list:
                try:
                    if input_list.index(num) is answer_list.index(num):
                        counter += 1
                except ValueError:
                    counter += 0
            self.hit = counter

        def victory_validator(input_list):
            if self.hit is 4:
                self.player_victory = True
                print('YOU WIN!!')

        return(blow_validator, hit_validator, victory_validator)

    def game_logic(self, input_txt):
        self.hit = 0
        self.blow = 0
        Game.array_validator(input_txt)

        input_list = [int(letter) for letter in input_txt]

        for validation in Game.answer_validator(self, input_list):
            validation(input_list)
        print("Hit: {0}, Blow: {1}".format(self.hit, self.blow))
