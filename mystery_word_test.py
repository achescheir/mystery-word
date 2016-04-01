import unittest
import mystery_word

class TestMysteryWord(unittest.TestCase):
    #
    # def test_assert_true(self):
    #     self.assertTrue(True)
    #
    # def test_assert_false(self):
    #     self.assertFalse(False)
    #
    # def test_assert_equal(self):
    #     self.assertEqual(1, 1)
    #
    # def test_assert_not_equal(self):
    #     self.assertNotEqual(1, 0)
    def test_parse_difficulty(self):
        self.assertEqual(mystery_word.parse_difficulty(''),'')
        self.assertEqual(mystery_word.parse_difficulty('e'),'easy')
        self.assertEqual(mystery_word.parse_difficulty('n'),'normal')
        self.assertEqual(mystery_word.parse_difficulty('h'),'hard')
        self.assertEqual(mystery_word.parse_difficulty('easy'),'easy')
        self.assertEqual(mystery_word.parse_difficulty('normal'),'normal')
        self.assertEqual(mystery_word.parse_difficulty('hard'),'hard')
        self.assertEqual(mystery_word.parse_difficulty('E'),'easy')
        self.assertEqual(mystery_word.parse_difficulty('N'),'normal')
        self.assertEqual(mystery_word.parse_difficulty('H'),'hard')
        self.assertEqual(mystery_word.parse_difficulty('Easy'),'easy')
        self.assertEqual(mystery_word.parse_difficulty('Normal'),'normal')
        self.assertEqual(mystery_word.parse_difficulty('Hard'),'hard')
        self.assertEqual(mystery_word.parse_difficulty('EASY'),'easy')
        self.assertEqual(mystery_word.parse_difficulty('NORMAL'),'normal')
        self.assertEqual(mystery_word.parse_difficulty('HARD'),'hard')
        self.assertEqual(mystery_word.parse_difficulty('b'),'')
        self.assertEqual(mystery_word.parse_difficulty('C'),'')
        self.assertEqual(mystery_word.parse_difficulty('1'),'')
        self.assertEqual(mystery_word.parse_difficulty('.'),'')
        self.assertEqual(mystery_word.parse_difficulty('sdf23'),'')
        self.assertEqual(mystery_word.parse_difficulty('Exit'),'easy')
        self.assertEqual(mystery_word.parse_difficulty('escape'),'easy')
        self.assertEqual(mystery_word.parse_difficulty('no'),'normal')
        self.assertEqual(mystery_word.parse_difficulty(' '),'')
        self.assertEqual(mystery_word.parse_difficulty('\t'),'')
        self.assertEqual(mystery_word.parse_difficulty('\n'),'')
        self.assertEqual(mystery_word.parse_difficulty('two words'),'')
        self.assertEqual(mystery_word.parse_difficulty('_'),'')
        self.assertEqual(mystery_word.parse_difficulty('\\'),'')

    def test_read_dictionary(self):
        word_list = mystery_word.read_dictionary()
        self.assertTrue(len(word_list)>0)
        self.assertTrue(len(word_list[0])>0)
        self.assertTrue(str(word_list[0]) is word_list[0])

    def test_get_word_easy(self):
        word_list=['easy','Easy','EASY','normals',"Normals","NORMALS","superhard","Superhard","SUPERHARD"]
        self.assertEqual(mystery_word.get_word(word_list,'easy'),'easy')

    def test_get_word_normal(self):
        word_list=['easy','Easy','EASY','normals',"Normals","NORMALS","superhard","Superhard","SUPERHARD"]
        self.assertEqual(mystery_word.get_word(word_list,'normal'),'normals')

    def test_get_word_hard(self):
        word_list=['easy','Easy','EASY','normals',"Normals","NORMALS","superhard","Superhard","SUPERHARD"]
        self.assertEqual(mystery_word.get_word(word_list,'hard'),'superhard')

    def test_get_wrong_guesses(self):
        secret_word = 'apple'
        guesses = ['q','w','r','t','y','u','i','o']
        self.assertEqual(mystery_word.get_wrong_guesses(secret_word, guesses),guesses)

    def test_time_up_too_many_misses(self):
        secret_word = 'apple'
        guesses = ['q','w','r','t','y','u','i','o']
        max_misses = 8
        self.assertTrue(mystery_word.is_time_up(secret_word,guesses,max_misses))

    def test_round_over_too_many_misses(self):
        secret_word = 'apple'
        guesses = ['q','w','r','t','y','u','i','o']
        max_misses = 8
        self.assertTrue(mystery_word.is_round_over(secret_word,guesses,max_misses))

    def test_word_is_guessed_simple(self):
        secret_word = 'apple'
        guesses = [x for x in secret_word]
        self.assertTrue(mystery_word.is_word_guessed(secret_word,guesses))

    def test_word_is_guessed_capitalized(self):
        secret_word = 'Apple'
        guesses = [x.lower() for x in secret_word]
        self.assertTrue(mystery_word.is_word_guessed(secret_word,guesses))

    def test_round_over_guessed(self):
        secret_word = 'apple'
        guesses = [x for x in secret_word]
        max_misses = 8
        self.assertTrue(mystery_word.is_round_over(secret_word,guesses,max_misses))

    def test_

if __name__ == '__main__':
    unittest.main()
