class HashTable:
    def __init__(self, capacity=200):
        """
        Initializes a HashTable with the given capacity.
        
        Args:
            capacity (int): The number of buckets in the hash table.
        """
        self.capacity = capacity
        self.table = [None] * capacity 

    def _hash(self, key):
        """
        Computes the hash index for a given key.
        
        Args:
            key: The key to hash.
        
        Returns:
            int: The hash index for the key.
        """
        return hash(key) % self.capacity
    
    def put(self, key):
        """
        Inserts the given key into the HashTable. Handles collisions using chaining.
        
        Args:
            key: The key to insert into the hash table.
        """
        hashed_index = self._hash(key)
        if self.table[hashed_index] is None:
            self.table[hashed_index] = []
        self.table[hashed_index].append(key)

    def find(self, key):
        """
        Checks if the given key is present in the HashTable.
        
        Args:
            key: The key to check for presence in the hash table.
        
        Returns:
            bool: True if the key is found, otherwise False.
        """
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        if bucket is None:
            return False 
        return key in bucket  

    def sum_of_unique_elements(self, nums):
        """
        Computes the sum of unique elements in the given list.
        
        Args:
            nums (list): The list of numbers.
        
        Returns:
            int: The sum of unique elements.
        """
        # Step 1: Create a hash table to store the frequency of each element
        frequency = {}
        
        # Step 2: Update the frequency of each element in the hash table
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        # Step 3: Initialize a variable to store the sum of unique elements
        unique_sum = 0
        
        # Step 4: Iterate through the hash table and sum up the unique elements
        for num, count in frequency.items():
            if count == 1:
                unique_sum += num
        
        # Step 5: Return the sum
        return unique_sum

# Usage example
nums1 = [1, 2, 3, 2]
ht = HashTable()
print(ht.sum_of_unique_elements(nums1))  # Output: 4

nums2 = [1, 2, 3, 4, 5]
print(ht.sum_of_unique_elements(nums2))  # Output: 15
