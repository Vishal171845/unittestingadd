import unittest


def add(x, y):
    return x+y
class MyApp(unittest.TestCase):

    def test_case1(self):
        a = 10
        b = 22
        result = add (a, b)
        self.assertEqual(a+b, result)

    def test_case2(self):
        a = 15.2
        b = 11.1
        result = add(a, b)
        self.assertEqual(a+b, result)
if __name__=="__main__":
    unittest.main()