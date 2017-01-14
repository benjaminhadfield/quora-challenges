"""
Python 3.5
Quora Challenge: Upvotes

Ben Hadfield, benjohnhadfield@gmail.com || benjamin.hadfield.14@ucl.ac.uk

Expected input
a b
i i i i ... (a times)
"""


class Upvotes:
    def __init__(self, n, k, data):
        if n < k or n is not len(data):
            raise AttributeError('Check the input to Upvotes.')

        self.n = n
        self.k = k
        self.data = data

    def count(self):
        """
        Takes the list of upvote data and returns a list of integers corresponding to the number of non-decreasing
        subranges within the window minus the number of non-increasing subranges within each window.
        """
        result = []
        offset = 0

        for i in range (self.n - self.k + 1):
            window = self.data[offset:offset + self.k]
            count_non_decreasing = self.count_non_decreasing(window)
            count_non_increasing = self.count_non_increasing(window)
            result.append(count_non_decreasing - count_non_increasing)

            offset += 1

        return result

    def print_count(self):
        """
        Performs self.count but prints the output to sdout, with each result on a new line.
        """
        result = self.count()
        for r in result:
            print(r)

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


# Get input lines
n, k = [int(i) for i in input().strip().split(' ')]
upvotes = input().strip().split(' ')

# Get the result
upvotes = Upvotes(n, k, upvotes)
upvotes.print_count()
