import unittest
from functions import remove_escapes
from functions import add_escapes

class TestStringMethods(unittest.TestCase):

    def test_remove_escapes(self):
        self.assertEqual(remove_escapes('hello no escapes here'),'hello no escapes here')
        self.assertEqual(remove_escapes('escape \\"quotation\\"'),'escape \"quotation\"')
        self.assertEqual(remove_escapes('escape escapes \\\\%'),'escape escapes \\%')
        self.assertEqual(remove_escapes('both \\"quot\\" \\\\!'),'both \"quot\" \\!') 

    def test_add_escapes(self):
        self.assertEqual(add_escapes('hello no escapes here'),'hello no escapes here')
        self.assertEqual(add_escapes('escape \"quotation\"'),'escape \\"quotation\\"')
        self.assertEqual(add_escapes('escape escapes \\%'),'escape escapes \\\\%')
        self.assertEqual(add_escapes('both \"quot\" \\!'),'both \\"quot\\" \\\\!') 


if __name__ == '__main__':
    unittest.main()