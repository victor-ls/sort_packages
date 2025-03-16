import unittest
from sort_packages import sort

class TestSortPackages(unittest.TestCase):
    def test_should_return_rejected_when_package_is_bulky_and_heavy(self):
        self.assertEqual(sort(100, 100, 100, 20), 'rejected')
    
    def test_should_return_special_when_package_is_bulky(self):
        self.assertEqual(sort(100, 100, 100, 19), 'special')
        
    def test_should_return_special_when_package_is_heavy(self):
        self.assertEqual(sort(10, 10, 10, 20), 'special')
    
    def test_should_return_standard_when_package_is_not_bulky_and_not_heavy(self):
        self.assertEqual(sort(10, 10, 10, 19), 'standard')
        
    def test_should_raise_value_error_when_any_input_is_not_numeric(self):
        with self.assertRaises(ValueError):
            sort('a', 10, 10, 10)
        with self.assertRaises(ValueError):
            sort(10, 'a', 10, 10)
        with self.assertRaises(ValueError):
            sort(10, 10, 'a', 10)
        with self.assertRaises(ValueError):
            sort(10, 10, 10, 'a')
    
    def test_should_raise_value_error_when_any_input_is_negative(self):
        with self.assertRaises(ValueError):
            sort(-1, 10, 10, 10)
        with self.assertRaises(ValueError):
            sort(10, -1, 10, 10)
        with self.assertRaises(ValueError):   
            sort(10, 10, -1, 10)
        with self.assertRaises(ValueError):
            sort(10, 10, 10, -1)

if __name__ == '__main__':
    unittest.main()
