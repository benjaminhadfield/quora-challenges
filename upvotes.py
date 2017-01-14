"""
Python 3.5
Quora Challenge: Upvotes

Ben Hadfield, benjohnhadfield@gmail.com || benjamin.hadfield.14@ucl.ac.uk
"""


class Upvotes:
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def count_non_decreasing(self, window):
        """Takes a window of numbers and returns the number of non-decreasing sub-ranges."""
        return self._count_using_function(window, 'is_non_decreasing')

    def count_non_increasing(self, window):
        """Takes a window of numbers and returns the number of non-decreasing sub-ranges."""
        return self._count_using_function(window, 'is_non_increasing')

    def _count_using_function(self, window, function):
        """Takes a window of numbers and a function to apply to the sub-ranges."""

        # Check we have the expected window size.
        if len(window) is not self.k:
            raise AttributeError(
                'Incorrect window size. Expected window size to be {0} but got {1}.'.format(
                    self.k, len(window)))

        # Window is okay :)
        count = 0
        func = getattr(Upvotes, str(function))

        for i in range(2, self.k + 1):
            offset = 0
            while offset + i <= len(window):
                if func(window[offset:offset + i]):
                    count += 1
                offset += 1

        return count

    @staticmethod
    def is_non_decreasing(list):
        """Takes an arbitrary list of numbers and returns a bool representing if that list is a non-decreasing list."""
        memo = list[0]
        for i in list:
            if i < memo:
                return False
            memo = i
        return True

    @staticmethod
    def is_non_increasing(list):
        """Takes an arbitrary list of numbers and returns a bool representing if that list is a non-decreasing list."""
        memo = list[0]
        for i in list:
            if i > memo:
                return False
            memo = i
        return True


print(Upvotes(5, 3).count_non_increasing([8, 4, 5]))
