# Author : qizles
# Small tool, implements the excercise on https://codingdojo.org/kata/FizzBuzz/ , which checks for all values
# from 1 to 100 if it is divisible by 5 or 3 or contains that digit, if so, the output is changed to pre defined
# strings, else the output for that number is the same value as the input.

import unittest

FIZZ_VALUE = 3
BUZZ_VALUE = 5


# Calculate FizzBuzz of single value
def fizz_buzz_value_of(value):
    fizz_buzz_value = ""
    if value % FIZZ_VALUE == 0 or str(FIZZ_VALUE) in str(value):
        fizz_buzz_value = "Fizz"
    if value % BUZZ_VALUE == 0 or str(BUZZ_VALUE) in str(value):
        fizz_buzz_value += "Buzz"
    if not fizz_buzz_value:
        fizz_buzz_value = str(value)
    return fizz_buzz_value


# Test class for FizzBuzz
class TestFizzBuzz(unittest.TestCase):
    def testFizzByDivisibility(self):
        self.assertEqual(fizz_buzz_value_of(42), 'Fizz', "Divisibility check for 'Fizz' fails")

    def testFizzByContains(self):
        self.assertEqual(fizz_buzz_value_of(13), 'Fizz', "Contains check for 'Fizz' fails")

    def testBuzzByDivisibility(self):
        self.assertEqual(fizz_buzz_value_of(20), 'Buzz', "Divisibility check for 'Buzz' fails")

    def testBuzzByContains(self):
        self.assertEqual(fizz_buzz_value_of(59), 'Buzz', "Contains check for 'Buzz' fails")

    def testFizzBuzzByDivisibility(self):
        self.assertEqual(fizz_buzz_value_of(60), 'FizzBuzz', "Divisibility check for 'FizzBuzz' fails")

    def testFizzBuzzByContains(self):
        self.assertEqual(fizz_buzz_value_of(53), 'FizzBuzz', "Contains check for 'FizzBuzz' fails")

    def testNonFizzOrBuzzValues(self):
        for j in [1, 4, 14, 22, 41, 62, 89, 98]:
            self.assertEqual(fizz_buzz_value_of(j), str(j), f"False reaction on non Fizz or Buzz number '{j}'")


# Run FizzBuzz from 1 to 100
if __name__ == '__main__':
    # unittest.main()
    for i in range(1, 101):
        print(fizz_buzz_value_of(i))
