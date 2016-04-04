import unittest
import mystery_word as mw

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
        self.assertEqual(mw.parse_difficulty(''),'')
        self.assertEqual(mw.parse_difficulty('e'),'easy')
        self.assertEqual(mw.parse_difficulty('n'),'normal')
        self.assertEqual(mw.parse_difficulty('h'),'hard')
        self.assertEqual(mw.parse_difficulty('easy'),'easy')
        self.assertEqual(mw.parse_difficulty('normal'),'normal')
        self.assertEqual(mw.parse_difficulty('hard'),'hard')
        self.assertEqual(mw.parse_difficulty('E'),'easy')
        self.assertEqual(mw.parse_difficulty('N'),'normal')
        self.assertEqual(mw.parse_difficulty('H'),'hard')
        self.assertEqual(mw.parse_difficulty('Easy'),'easy')
        self.assertEqual(mw.parse_difficulty('Normal'),'normal')
        self.assertEqual(mw.parse_difficulty('Hard'),'hard')
        self.assertEqual(mw.parse_difficulty('EASY'),'easy')
        self.assertEqual(mw.parse_difficulty('NORMAL'),'normal')
        self.assertEqual(mw.parse_difficulty('HARD'),'hard')
        self.assertEqual(mw.parse_difficulty('b'),'')
        self.assertEqual(mw.parse_difficulty('C'),'')
        self.assertEqual(mw.parse_difficulty('1'),'')
        self.assertEqual(mw.parse_difficulty('.'),'')
        self.assertEqual(mw.parse_difficulty('sdf23'),'')
        self.assertEqual(mw.parse_difficulty('Exit'),'easy')
        self.assertEqual(mw.parse_difficulty('escape'),'easy')
        self.assertEqual(mw.parse_difficulty('no'),'normal')
        self.assertEqual(mw.parse_difficulty(' '),'')
        self.assertEqual(mw.parse_difficulty('\t'),'')
        self.assertEqual(mw.parse_difficulty('\n'),'')
        self.assertEqual(mw.parse_difficulty('two words'),'')
        self.assertEqual(mw.parse_difficulty('_'),'')
        self.assertEqual(mw.parse_difficulty('\\'),'')

    def test_read_dictionary(self):
        word_list = mw.read_dictionary()
        self.assertTrue(len(word_list)>0)
        self.assertTrue(len(word_list[0])>0)
        self.assertTrue(str(word_list[0]) is word_list[0])

    def test_get_sublist_easy(self):
        word_list=['easy','Easy','EASY','normals',"Normals","NORMALS","superhard","Superhard","SUPERHARD"]
        self.assertEqual(mw.get_sublist(word_list,'easy'),['easy','Easy','EASY'])

    def test_get_sublist_normal(self):
        word_list=['easy','Easy','EASY','normals',"Normals","NORMALS","superhard","Superhard","SUPERHARD"]
        self.assertEqual(mw.get_sublist(word_list,'normal'),['normals',"Normals","NORMALS"])

    def test_get_sublist_hard(self):
        word_list=['easy','Easy','EASY','normals',"Normals","NORMALS","superhard","Superhard","SUPERHARD"]
        self.assertEqual(mw.get_sublist(word_list,'hard'),["superhard","Superhard","SUPERHARD"])

    def test_get_word(self):
        self.assertEqual(mw.get_word(['EASY',"EASY"]),'easy')

    def test_get_wrong_guesses_form(self):
        self.assertEqual(mw.get_wrong_guesses_form(['a','b','c'],5),'[abc--]')

    def test_letter_is_in_collection_string(self):
        self.assertTrue(mw.letter_is_in_collection('s','sdfwfsdfw'))

    def test_letter_is_in_collection_list(self):
        self.assertTrue(mw.letter_is_in_collection('s',['s','d','f']))

    def test_letter_is_in_collection_false(self):
        self.assertFalse(mw.letter_is_in_collection('s','dfwfdfw'))

    def test_get_word_print_form(self):
        self.assertEqual(mw.get_word_print_form("goofy",['o','y']),'_ O O _ Y')

    def test_cleanup_input_empty(self):
        self.assertEqual(mw.cleanup_input(''),'')

    def test_cleanup_input_too_long(self):
        self.assertEqual(mw.cleanup_input('asd'),"")

    def test_cleanup_input_capital(self):
        self.assertEqual(mw.cleanup_input('A'),'a')

    def test_cleanup_input_lowercase(self):
        self.assertEqual(mw.cleanup_input('a'),'a')

    def test_cleanup_input_number(self):
        self.assertEqual(mw.cleanup_input('9'),'')

    def test_word_is_guessed_simple(self):
        secret_word = 'apple'
        guesses = [x for x in secret_word]
        self.assertTrue(mw.is_word_guessed(secret_word,guesses))

    def test_word_is_guessed_capitalized(self):
        secret_word = 'Apple'
        guesses = [x.lower() for x in secret_word]
        self.assertTrue(mw.is_word_guessed(secret_word,guesses))

    def test_get_wrong_guesses_all(self):
        secret_word = 'apple'
        guesses = ['q','w','r','t','y','u','i','o']
        self.assertEqual(mw.get_wrong_guesses(secret_word, guesses),guesses)

    def test_get_wrong_guesses_some(self):
        secret_word = 'apple'
        guesses = ['q','w','r','t','y','u','i','o','p']
        self.assertEqual(mw.get_wrong_guesses(secret_word, guesses),guesses[:-1])

    def test_get_wrong_guesses_none(self):
        secret_word = 'apple'
        guesses = ['p']
        self.assertEqual(mw.get_wrong_guesses(secret_word, guesses),[])

    def test_time_up_too_many_misses(self):
        secret_word = 'apple'
        guesses = ['q','w','r','t','y','u','i','o']
        max_misses = 8
        self.assertTrue(mw.is_time_up(secret_word,guesses,max_misses))

    def test_round_over_too_many_misses(self):
        secret_word = 'apple'
        guesses = ['q','w','r','t','y','u','i','o']
        max_misses = 8
        self.assertTrue(mw.is_round_over(secret_word,guesses,max_misses))


    def test_round_over_guessed(self):
        secret_word = 'apple'
        guesses = [x for x in secret_word]
        max_misses = 8
        self.assertTrue(mw.is_round_over(secret_word,guesses,max_misses))

if __name__ == '__main__':
    unittest.main()
