# Dutch National Flag problem : 
'''
(Level: Medium) Dutch National Flag Problem: Given an array of integers A and an index I, rearrange A in the following order: 
[Elements less than A[I], elements equal to A[I], elements greater than A[I]]

Input -> An array of integers.
Output -> An array of integers 

Ex:
input -> dnf([1, 0, 2, 3, 0, 1], 2)
ouput -> [1, 0, 1, 0, 2, 3]
'''
def dnf(array, x):
    low = -1
    mid = -1
    high = len(array)
    
    target = array[x]
    
    while mid + 1 < high:
        
        if array[mid + 1] < target:
            low_copy = array[low + 1]
            mid_copy = array[mid + 1]
            array[low + 1] = mid_copy
            array[mid + 1] = low_copy
            low += 1
            mid += 1
            
        elif array[mid + 1] == target:
            mid += 1
            
        elif array[mid + 1] > target:
            mid_copy = array[mid + 1]
            high_copy = array[high - 1]
            array[mid + 1] = high_copy
            array[high -1] = mid_copy
            high -= 1
            
    return array
a = dnf([1, 0, 2, 3, 0, 1], 2)
print(a)