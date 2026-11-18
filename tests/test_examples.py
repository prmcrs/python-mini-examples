"""Unit tests using only Python's standard library."""
import unittest
from datetime import date

from programs.prime.prime import is_prime, prime_factors, primes_up_to
from programs.age_calculator.age_calculator import calculate_age, calculate_decade
from programs.emissions.emissions import calculate_co_emission
from programs.basic_number_op.basic_number_op import add, multiply_three, comparisons


class PrimeTests(unittest.TestCase):
    def test_primality(self):
        self.assertEqual([is_prime(n) for n in (-3, 0, 1, 2, 7, 9, 49)],
                         [False, False, False, True, True, False, False])

    def test_factorization(self):
        self.assertEqual(prime_factors(84), [2, 2, 3, 7])
        self.assertEqual(prime_factors(13), [13])
        for number in (-1, 0, 1):
            with self.subTest(number=number):
                with self.assertRaises(ValueError):
                    prime_factors(number)

    def test_listing(self):
        self.assertEqual(primes_up_to(10), [2, 3, 5, 7])
        self.assertEqual(primes_up_to(1), [])


class AgeTests(unittest.TestCase):
    def test_before_and_after_birthday(self):
        self.assertEqual(calculate_age(date(2000, 12, 1), date(2026, 11, 18)), 25)
        self.assertEqual(calculate_age(date(2000, 1, 1), date(2026, 11, 18)), 26)

    def test_future_date(self):
        with self.assertRaises(ValueError):
            calculate_age(date(2027, 1, 1), date(2026, 11, 18))

    def test_decade(self):
        self.assertEqual(calculate_decade(date(1997, 5, 1)), 1990)


class EmissionsTests(unittest.TestCase):
    def test_threshold(self):
        self.assertEqual(calculate_co_emission(34, 10), (3.4, True))
        self.assertEqual(calculate_co_emission(40, 10), (4.0, False))

    def test_invalid_values(self):
        for grams, miles in ((1, 0), (1, -2), (-1, 10), (float("nan"), 10)):
            with self.subTest(grams=grams, miles=miles):
                with self.assertRaises(ValueError):
                    calculate_co_emission(grams, miles)


class ArithmeticTests(unittest.TestCase):
    def test_arithmetic(self):
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(multiply_three(2, -3, 4), -24)

    def test_comparisons(self):
        self.assertIn("2 < 3", comparisons(2, 3))
        self.assertIn("3 == 3", comparisons(3, 3))


if __name__ == "__main__":
    unittest.main()
