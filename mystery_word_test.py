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
        self.assertTrue(len(word_list[0])>0))
        self.assertTrue(str(word_list[0]) is word_list[0])

    def test_get_word(self):
        word_list=['easy','EEasy','EASY','norml',"Norml","NORML","hardest","Hardest","HARDEST"]
        self.assertEqual(mystery_word.get_word([word_list],'easy').lower(),'easy')

    def test_get_word(self):
        word_list=['easy','EEasy','EASY','norml',"Norml","NORML","hardest","Hardest","HARDEST"]
        self.assertEqual(mystery_word.get_word([word_list],'normal').lower(),'norml')

    def test_get_word(self):
        word_list=['easy','EEasy','EASY','norml',"Norml","NORML","hardest","Hardest","HARDEST"]
        self.assertEqual(mystery_word.get_word([word_list],'hard').lower(),'hard')


if __name__ == '__main__':
    unittest.main()
