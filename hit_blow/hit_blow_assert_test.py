import unittest
import hit_blow_assert as testee


class HitBlowTest(unittest.TestCase):

    def test_to_generate_answer_list(self):
        ''' len is 4 and no duplication'''
        a_list = testee.Game().answer_list
        self.assertEqual(len(a_list), 4)
        self.assertEqual(len(a_list), len(set(a_list)))


if __name__ == '__main__':
    unittest.main()
