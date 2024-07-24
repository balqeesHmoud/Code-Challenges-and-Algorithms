def sum_of_unique_elements(nums):
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
print(sum_of_unique_elements(nums1))  # Output: 4

nums2 = [1, 2, 3, 4, 5]
print(sum_of_unique_elements(nums2))  # Output: 15
