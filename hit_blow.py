import numpy as np


class Game(object):
    """docstring for Game"""

    def __init__(self):
        super(Game, self).__init__()
        self.game_array = None
        self.user_input = None
        self.game_array = None
        self.player_victory = False

    def get_user_input(self):
        answer_txt = raw_input("> Guess Number:  ")
        answer_ar = list(answer_txt)
        self.user_input = map(int, answer_ar)

    def check_array(self):
        hit = 0
        blow = 0

        if len(list(set(self.user_input))) != 4:
            raise InvalidGuessError()

        for num in self.user_input:
            if num not in np.arange(10):
                raise InvalidGuessError()

        for counter in range(0, 4):
            self.user_input[counter]
            if self.user_input[counter] == self.game_array[counter]:
                hit += 1
            elif self.user_input[counter] in self.game_array:
                blow += 1

        if hit is 4:
            self.player_victory = True
            print "CONGRATURATION!!"
        else:
            print "Hit: %s, Blow: %s" % (hit, blow)

    def generate_game_array(self):
        array = np.arange(10)
        np.random.shuffle(array)
        self.game_array = array[0:4]
        print self.game_array


class InvalidGuessError(Exception):
    """docstring for InvalidGuess"""

    def __init__(self, array):
        self.arg = array

game = Game()
game.generate_game_array()

while game.player_victory is False:
    try:
        game.get_user_input()
        game.check_array()
    except InvalidGuessError:
        print "Try again, your guess was invalid."
