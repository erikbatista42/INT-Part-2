# Majority Element
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Input -> Array Ints
Output -> Integer

Ex:
input -> majorityElement([2,2,1,1,1,2,2])
ouput -> 2
'''
def majorityElement(nums):
    length = len(nums)
    majority = length//2
    table = {}
    # histogram of nums
    for num in nums:
        table[num] = table.get(num, 0) + 1
        if table[num] > majority:
            return num

a = majorityElement([2,2,1,1,1,2,2])
print(a)