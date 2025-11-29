class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative.")
        self._capacity = capacity
        self._contents = 0

    def __str__(self):
        return "🍪" * self._contents

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self._contents + n > self._capacity:
            raise ValueError("Exceeds jar capacity.")
        self._contents += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if n > self._contents:
            raise ValueError("Not enough cookies to withdraw.")
        self._contents -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._contents
