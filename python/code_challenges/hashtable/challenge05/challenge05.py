class HashTable:
    """
    A simple hash table implementation for storing and querying elements.
    """

    def __init__(self, size=100):
        """
        Initializes the hash table with a fixed size and empty buckets.

        :param size: The size of the hash table. Default is 100.
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """
        Computes the hash index for a given key.

        :param key: The key to hash.
        :return: The hash index.
        """
        return hash(key) % self.size

    def insert(self, key):
        """
        Inserts a key into the hash table if it is not already present.

        :param key: The key to insert.
        """
        hash_index = self._hash(key)
        if key not in self.table[hash_index]:
            self.table[hash_index].append(key)

    def contains(self, key):
        """
        Checks if a key is present in the hash table.

        :param key: The key to check.
        :return: True if the key is present, False otherwise.
        """
        hash_index = self._hash(key)
        return key in self.table[hash_index]


def array_intersection(arr1, arr2):
    """
    Finds the intersection of two arrays, returning a list of unique elements that appear in both arrays.

    :param arr1: The first array.
    :param arr2: The second array.
    :return: A list of unique elements that are in both arrays.
    """
    hash_table = HashTable()
    result_set = set()

    # Insert elements of the first array into the hash table
    for num in arr1:
        hash_table.insert(num)

    # Check for common elements in the second array
    for num in arr2:
        if hash_table.contains(num):
            result_set.add(num)

    return list(result_set)


# Example Usage
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 1], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4]),
        ([1, 2, 3], [4, 5, 6]),
        ([1, 2, 2, 1, 3], [2, 2, 3, 4]),
        ([1], [1, 1, 1, 1])
    ]

    for arr1, arr2 in test_cases:
        result = array_intersection(arr1, arr2)
        print(f"Array 1: {arr1}")
        print(f"Array 2: {arr2}")
        print(f"Result: {result}\n")
