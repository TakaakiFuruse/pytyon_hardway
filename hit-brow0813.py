import random
import re


class HitBrowGame():
    """docstring for HitBrowGame"""

    def __init__(self):
        self.correct_answer = self.generate_answer()
        self.user_victory = False
        self.hit = 0
        self.brow = 0

    def take_input(self):
        self.hit = 0
        self.brow = 0
        user_answer = input('> Your Guess?  ')
        self.user_answer = [int(num) for num in user_answer]

    def generate_answer(self):
        answer = [num for num in range(1, 10)]
        random.shuffle(answer)
        return answer[0:4]

    def build_user_answer_validator(self):
        def digit_checker(self):
            for letter in self.user_answer:
                if re.search('\D', str(letter)):
                    raise ValueError('List include non digit letter.')

        def answer_length_checker(self):
            if len(self.user_answer) is not 4:
                raise ValueError('Answer should be in 4 length long.')

        def number_duplication_checker(self):
            if len(set(self.user_answer)) is not 4:
                raise ValueError('Answer contains dupulicated letter/s.')

        def hit_brow_chekcer(self):
            for index, num in enumerate(self.user_answer):
                if self.correct_answer[index] is num:
                    self.hit += 1
                elif num in self.correct_answer:
                    self.brow += 1

        return [digit_checker, answer_length_checker,
                number_duplication_checker, hit_brow_chekcer]

    def victory_checker(self):
        brow = self.brow
        hit = self.hit
        if hit is 4:
            self.user_victory = 1
            print('You Win!!')
        else:
            print(f"hit is {hit}, blow is {brow}")

    def validate_answer(self):
        for validator in self.build_user_answer_validator():
            validator(self)

game = HitBrowGame()

while game.user_victory is False:
    game.take_input()
    game.validate_answer()
    game.victory_checker()

