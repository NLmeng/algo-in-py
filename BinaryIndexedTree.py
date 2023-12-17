class BinaryIndexedTree:
    def __init__(self, size):
        """
        Initialize the BIT with a given size. Initially, a list of zeros.
        """
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        """
        Update the BIT at a given index by a delta value. Propagates the change
        up the tree to ensure that all relevant sums/counts/frequencies are updated.
        :param index: The 1-based index in the array to update.
        :param delta: The value to add at the given index.
        """
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index  # Move to the next index that needs to be updated.

    def query(self, index):
        """
        Query the cumulative sums/counts/frequencies up to a given index. Aggregates values from
        different parts of the tree to compute the sum.
        :param index: The 1-based index up to which the cumulative sum is computed.
        :return: The cumulative sum up to the given index.
        """
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index  # Move to the next contributing index.
        return sum

    def range_query(self, start, end):
        """
        Perform a range query to get the sum of values in a specific range.
        :param start: The start index of the range (inclusive).
        :param end: The end index of the range (inclusive).
        :return: The sum of values in the range [start, end].
        """
        return self.query(end) - self.query(start - 1)