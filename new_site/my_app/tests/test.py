import unittest


# first test

def operations(a, b, c):
    if c == '+':
        return a + b
    if c == '-':
        return a - b
    if c == '*':
        return a * b
    if c == '/':
        return a / b


class test_1(unittest.TestCase):
    def test_plus(self):
        result = operations(9, 3, '+')

        if result == 13:
            message = "the value is true"
        else:
            message = "the value is not true"

        value = True

        self.assertTrue(value, message)

    def test_minus(self):
        result = operations(9, 3, '-')
        self.assertEqual(6, result)

        print("test_minus works good \n")

    def test_multiplication(self):
        result = operations(9, 3, '*')
        self.assertEqual(27, result)

        print("test_multiplication works good \n")

    def test_division(self):
        result = operations(9, 3, '/')
        self.assertEqual(3, result)

        print("test_division works good \n")


if __name__ == '__main__':
    unittest.main()


# second test

class test_2(unittest.TestCase):
    word_1 = 'bad'
    word_2 = 'good'

    def test_check(self):
        length_1 = len(self.word_1)
        length_2 = len(self.word_2)

        if length_1 > length_2:
            result = length_1

            self.assertEqual(len(self.word_1), result)
            print(self.word_1 + ' is greater than ' + self.word_2)

        elif length_1 < length_2:
            result = length_2

            self.assertEqual(len(self.word_2), result)
            print(self.word_1 + ' is smaller than ' + self.word_2)

        else:

            self.assertEqual(len(self.word_1), len(self.word_2))
            print(self.word_1 + ' is equal to ' + self.word_2)


# third test

class test_3(unittest.TestCase):
    first = 'street'

    def test_check(self):
        last = self.first + 's'

        self.assertTrue(True)
        print('plural form of ' + self.first + ' is ' + last)
