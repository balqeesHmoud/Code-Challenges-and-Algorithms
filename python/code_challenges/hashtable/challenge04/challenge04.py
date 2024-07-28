class HashTable:
    def __init__(self, capacity=200):
        """
        Initialize the hash table with a given capacity.
        :param capacity: The number of buckets in the hash table.
        """
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key):
        """
        Compute the hash index for a given key.
        :param key: The key to hash.
        :return: The hash index.
        """
        return hash(key) % self.capacity

    def put(self, key):
        """
        Insert a key into the hash table.
        :param key: The key to insert.
        """
        hashed_index = self._hash(key)
        if self.table[hashed_index] is None:
            self.table[hashed_index] = []
        self.table[hashed_index].append(key)

    def find(self, key):
        """
        Check if a key exists in the hash table.
        :param key: The key to find.
        :return: True if the key exists, otherwise False.
        """
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        return bucket is not None and key in bucket

    @staticmethod
    def sort_people(names, heights):
        """
        Reorder the people based on their heights in descending order.
        :param names: List of names.
        :param heights: List of heights corresponding to names.
        :return: List of names reordered by heights in descending order.
        """
        # Combine names and heights into a list of tuples
        combined = list(zip(names, heights))
        # Sort the combined list by heights in descending order
        combined_sorted = sorted(combined, key=lambda x: x[1], reverse=True)
        # Extract the names from the sorted list
        sorted_names = [name for name, height in combined_sorted]
        return sorted_names

# Example usage
if __name__ == "__main__":
    names = ["Tom", "Jerry", "Spike"]
    heights = [180, 160, 170]
    print(HashTable.sort_people(names, heights))  # Output: ["Tom", "Spike", "Jerry"]
