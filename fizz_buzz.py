# qizles
import unittest


def fizz_buzz_value_of(value):
    fizz_buzz_value = ""
    if value % 3 == 0 or '3' in str(value):
        fizz_buzz_value = "Fizz"
    if value % 5 == 0 or '5' in str(value):
        fizz_buzz_value += "Buzz"
    if not fizz_buzz_value:
        fizz_buzz_value = str(value)
    return fizz_buzz_value


class TestFizzBuzz(unittest.TestCase):
    def test_fizz_by_divisibility(self):
        self.assertEqual(fizz_buzz_value_of(42), 'Fizz', "Should be 'Fizz'")

    def test_fizz_by_contains(self):
        self.assertEqual(fizz_buzz_value_of(13), 'Fizz', "Should be 'Fizz'")

    def test_buzz_by_divisibility(self):
        self.assertEqual(fizz_buzz_value_of(20), 'Buzz', "Should be 'Buzz'")

    def test_buzz_by_contains(self):
        self.assertEqual(fizz_buzz_value_of(59), 'Buzz', "Should be 'Buzz'")

    def test_fizz_buzz_by_divisibility(self):
        self.assertEqual(fizz_buzz_value_of(60), 'FizzBuzz', "Should be 'FizzBuzz'")

    def test_fizz_buzz_by_contains(self):
        self.assertEqual(fizz_buzz_value_of(53), 'FizzBuzz', "Should be 'FizzBuzz'")

    def test_non_fizz_buzz_values(self):
        for j in [1, 4, 14, 22, 41, 62, 89, 98]:
            self.assertEqual(fizz_buzz_value_of(j), str(j), f"Should be '{j}'")


if __name__ == '__main__':
    # unittest.main()
    for i in range(1, 101):
        print(fizz_buzz_value_of(i))
