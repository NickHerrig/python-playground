import unittest
import bankaccount

class TestBankaccount(unittest.TestCase):
    
    def test_balance(self):
        testaccount = bankaccount.Account(owner='Nick')
        result = testaccount.balance
        self.assertEqual(result, int(0))

    def test_owner(self):
        testaccount = bankaccount.Account(owner='Nick')
        result = testaccount.owner
        self.assertEqual(result, 'Nick')

if __name__ == '__main__':
    unittest.main()
