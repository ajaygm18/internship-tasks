import unittest

def add(a, b):
    return a + b

def divide(a, b):

    if b == 0:
        raise ValueError("Can't Divide by Zero")
    return a / b

class TestMathOperations(unittest.TestCase):

    def setUp(self):
        self.a = 5
        self.b = 10
        print("Setting UP resources")

    def tearDown(self):
        print("Cleaning up resources")
        del self.a, self.b

    def test_add(self):
        result = add(self.a, self.b)
        self.assertEqual(result, 15)

    def test_divide(self):
        result = divide(self.a, self.b)
        self.assertEqual(result, 0.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)


if __name__ == '__main__':
    unittest.main()

