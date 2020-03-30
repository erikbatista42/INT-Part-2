# Given an array with n objects colored Red, White or Blue, sort them so that objects of the same color are adjacent, with the colors in the order Red, White and Blue. Assume the colors are given as numbers - 0 (Red), 1 (White) and 2 (Blue).

'''
Input -> Array of Integers
Output -> Array of Integers 

Ex:
input -> red_blue_white([1,0,1,2,1,0,1,2])
ouput -> [0, 0, 1, 1, 1, 1, 2, 2]
'''

def swap(a, pointer_one, pointer_two):
    a[pointer_one], a[pointer_two] = a[pointer_two], a[pointer_one]
    
    
def red_blue_white(a):
    # Sort the given array containing numbers 1s, 2s, and 3s.
    low = -1
    mid = 0
    high = len(a)
    
    while mid < high:
        pivot = mid + 1
        
        if a[pivot] == 0:
            swap(a, pivot, low + 1)
            low += 1
            mid += 1
        if a[pivot] == 1:
            mid += 1
        if a[pivot] == 2:
            if a[high-1] == 2:
                high -= 1
                continue
            else:
                swap(a, pivot, high-1)       
    return  a

test = red_blue_white([1,0,1,2,1,0,1,2])
print(test)