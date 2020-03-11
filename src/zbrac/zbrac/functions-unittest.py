import unittest
from functions import remove_escapes
from functions import add_escapes
from functions import get_matched_entries
from functions import create_own_list
from functions import list_to_dict
from functions import replace_from_dictionary

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

    def test_get_matched_entries(self):
        text = """This is [[a \"test\" file]]. 
               Things there should be a bracket ([) in the output and there should be a [[replaced text]]."""
        no_entries_text = """This is [[a \"test\" file. 
                             Things there should be a bracket ([) in the output and there should be a replaced text."""
        entries = ['[[a \"test\" file]]','[[replaced text]]']
        self.assertEqual(get_matched_entries(text),entries)
        self.assertFalse(get_matched_entries(no_entries_text))

    def test_create_own_list(self):
        list = ['[[a \"test\" file]]','[[replaced text]]']
        empty_list = False
        self.assertEqual(create_own_list(list),[['[[a "test" file]]','[[replaced text]]'],['a "test" file','replaced text']])
        self.assertFalse(create_own_list(empty_list))

    def test_list_to_dict(self):
        list = [['[[a "test" file]]','[[replaced text]]'],['a "test" file','replaced text']]
        list2 = [['[[a "test" file]]','[[replaced text]]'],['a "test" file']]
        no_list = 45
        self.assertEqual(list_to_dict(list),{'[[a "test" file]]':'a "test" file','[[replaced text]]':'replaced text'})
        self.assertEqual(list_to_dict(list2),{'[[a "test" file]]':'a "test" file'})
        self.assertRaises(Exception, list_to_dict, [no_list])

    def test_replace_from_dictionary(self):
        text = """This is [[a \"test\" file]]. Things there should be a bracket ([) in the output and there should be a [[replaced text]]."""
        dict = {'[[a \"test\" file]]':'new \"text\"','[[replaced text]]':'random text'}
        target_text = """This is new \"text\". Things there should be a bracket ([) in the output and there should be a random text."""
        self.assertEqual(replace_from_dictionary(dict,text),target_text)

if __name__ == '__main__':
    unittest.main()