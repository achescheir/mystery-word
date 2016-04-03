import unittest
import evil_mystery_word as emw

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
    def test_get_signature_empty(self):
        self.assertEqual(emw.get_signature('battleship',[]),'__________')

    def test_get_signature_partial(self):
        self.assertEqual(emw.get_signature('battleship',['b','a','t','h']),'batt___h__')

    def test_get_signature_full(self):
        self.assertEqual(emw.get_signature('battleship',[x for x in 'battleship']),'battleship')

    def test_get_signature_mixed(self):
        self.assertEqual(emw.get_signature('battleship',['b','x','t','h']),'b_tt___h__')

    def test_count_signatures(self):
        self.assertEqual(emw.get_all_signatures(['bat','cat','bam'],['a','t']),{'_at':['bat','cat'],'_a_':['bam']})

    def test_evaluate_guess(self):
        test_list =['bat','cat','bam']
        test_guesses = ['a','t']
        self.assertEqual(emw.evaluate_guess(test_list,test_guesses),'_at')

    def test_get_candidates(self):
        test_list =['bat','cat','bam','']
        test_guesses = ['a','t']
        self.assertEqual(emw.get_candidates(test_list,test_guesses,'_at'),['bat','cat'])
        self.assertTrue(test_list == ['bat','cat','bam'])

if __name__ == '__main__':
    unittest.main()
