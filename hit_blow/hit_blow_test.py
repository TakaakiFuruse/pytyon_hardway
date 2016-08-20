import unittest
import hit_blow_logic as testee
import itertools


class HitBlowTest(unittest.TestCase):

    def test_to_generate_answer_list(self):
        game = testee.Game()
        ''' len is 4 and no duplication'''
        for _ in itertools.repeat(None, 4):
            game.generate_answer_list()
            a_list = game.answer_list
            self.assertEqual(len(a_list), 4)
            self.assertEqual(len(a_list), len(set(a_list)))

    def test_game_logic(self):
        game = testee.Game()
        game.answer_list = [1, 2, 3, 4]

        "All Correct"
        game = testee.Game()
        game.answer_list = [1, 2, 3, 4]
        game.game_logic('1234')
        self.assertEqual(game.hit, 4)
        self.assertEqual(game.blow, 0)
        self.assertEqual(game.player_victory, True)

        "Hit2 Blow2"
        game = testee.Game()
        game.answer_list = [1, 2, 3, 4]
        game.game_logic('2134')
        self.assertEqual(game.hit, 2)
        self.assertEqual(game.blow, 2)
        self.assertEqual(game.player_victory, False)

        "Hit0 Blow4"
        game = testee.Game()
        game.answer_list = [1, 2, 3, 4]
        game.game_logic('4321')
        self.assertEqual(game.hit, 0)
        self.assertEqual(game.blow, 4)
        self.assertEqual(game.player_victory, False)

        "Duplicated num raises Error"
        game = testee.Game()
        game.answer_list = [1, 2, 3, 4]
        with self.assertRaises(AssertionError):
             game.game_logic('4444')

        "Long num raises Error"
        game = testee.Game()
        game.answer_list = [1, 2, 3, 4]
        with self.assertRaises(AssertionError):
             game.game_logic('12345')

if __name__ == '__main__':
    unittest.main()
