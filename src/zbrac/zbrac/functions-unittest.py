import unittest
from functions import remove_escapes

class TestStringMethods(unittest.TestCase):

    def test_remove_escapes(self):
        self.assertEqual(remove_escapes('hello no escapes here'),'hello no escapes here')
        self.assertEqual(remove_escapes('normal escape \\!!'),'normal escape \!!')
        self.assertEqual(remove_escapes('double escapes \\\\%'),'double escapes \\%')
        self.assertEqual(remove_escapes('both \\"" \\\\5678'),'both \"" \\5678')
        
    

if __name__ == '__main__':
    unittest.main()