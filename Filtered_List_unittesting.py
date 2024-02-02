import unittest

def list_filter_function(list):
    if len(list) % 10 != 0:
        raise ValueError("List length is not a multiple of 10.")

    final_list = []
    for i in range(len(list)):
        if (i + 1) % 2 != 0 and (i + 1) % 3 != 0:
            final_list.append(list[i])

    return final_list

class TestFilterList(unittest.TestCase):

    def test_multiple_of_10(self):
        self.assertEqual(list_filter_function([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 5, 7])

    def test_not_multiple_of_10(self):
        with self.assertRaises(ValueError): 
            list_filter_function([1, 2, 3, 4, 5])

    def test_empty_list(self):
        with self.assertRaises(ValueError): 
            list_filter_function([])

    def test_list_with_identical_elements(self):
        self.assertEqual(list_filter_function([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [1])

    def test_list_with_negative_numbers(self):
        self.assertEqual(list_filter_function([-2, -3, -4, -5, -6, -7, -8, -9, -10, -11]), [-5, -7])

if __name__ == '__main__':
    unittest.main()
