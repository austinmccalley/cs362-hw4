import unittest
import name 


class test_fullName(unittest.TestCase):
    
    def testFullName(self):
        self.assertEqual(name.fullName('Bob', 'Jones'), 'Bob Jones')
    
    def testNoFirstName(self):
        self.assertRaises(AssertionError, name.fullName, '', 'Jones')

    def testNoLastName(self):
        self.assertRaises(AssertionError, name.fullName, 'Bob', '')

    def testUnicode(self):
        self.assertEqual(name.fullName('♥', '|:'), '♥ |:')

    def testAccents(self):
        self.assertEqual(name.fullName('Benito Pérez','Galdós'), 'Benito Pérez Galdós')

if __name__ == '__main__':
    unittest.main()
