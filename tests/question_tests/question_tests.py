#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import use_local_variable
class Test_Config(unittest.TestCase):

    #def test_question_a_config(self):
        #self.assertEqual(True, test_config())
    
    def test_use_local_variable(self):
        num = 100

        use_local_variable(num)

        self.assertEqual(num, 100)

    #def test_reverse_string(self):
        #self.assertEqual(reverse_string('hello world'), 'dlrow olleh')

    #def test_get_person_category(self):
        #self.assertEqual(get_person_category(1), 'Infant')
        #self.assertEqual(get_person_category(2), 'Child')
        #self.assertEqual(get_person_category(14), 'Teenager')
        #self.assertEqual(get_person_category(20), 'Adult')



