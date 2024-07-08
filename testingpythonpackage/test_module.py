import unittest
from testingpythonpackage.module import python_package_test
class TestModule(unittest.TestCase):
    def test_python_package_test(self):
        self.assertEqual(python_package_test(), "Python package test")

if __name__ == '__main__':
    unittest.main()