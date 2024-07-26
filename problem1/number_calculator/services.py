# number_calculator/services.py
from collections import deque
import random
import time

class NumberService:
    def __init__(self, window_size=10):
        self.window_size = window_size
        self.numbers = deque(maxlen=window_size)

    def fetch_numbers(self, number_type):
        # Placeholder: fetch from a third-party source
        # Simulate this with random values for simplicity
        if number_type == 'p':
            numbers = self._get_primes()
        elif number_type == 'f':
            numbers = self._get_fibonacci()
        elif number_type == 'e':
            numbers = self._get_evens()
        elif number_type == 'r':
            numbers = self._get_randoms()
        else:
            return []

        return numbers

    def _get_primes(self):
        # Example implementation
        primes = []
        candidate = 2
        while len(primes) < 10:
            if all(candidate % p != 0 for p in primes):
                primes.append(candidate)
            candidate += 1
        return primes

    def _get_fibonacci(self):
        # Example implementation
        fibs = [0, 1]
        while len(fibs) < 10:
            fibs.append(fibs[-1] + fibs[-2])
        return fibs

    def _get_evens(self):
        return list(range(2, 2 + 2 * 10, 2))

    def _get_randoms(self):
        return [random.randint(1, 100) for _ in range(10)]

    def add_numbers(self, new_numbers):
        for number in new_numbers:
            if number not in self.numbers:
                self.numbers.append(number)

    def get_average(self):
        if len(self.numbers) == 0:
            return 0
        return sum(self.numbers) / len(self.numbers)

    def process_numbers(self, number_type):
        start_time = time.time()
        new_numbers = self.fetch_numbers(number_type)
        elapsed_time = time.time() - start_time
        if elapsed_time > 0.5:
            return {'error': 'Request took too long'}

        prev_state = list(self.numbers)
        self.add_numbers(new_numbers)
        curr_state = list(self.numbers)
        avg = self.get_average()

        return {
            'windowPrevState': prev_state,
            'windowCurrState': curr_state,
            'numbers': new_numbers,
            'avg': avg
        }
