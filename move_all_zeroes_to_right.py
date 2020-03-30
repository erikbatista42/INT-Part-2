# Move all zeroes to the end of the given integer array

'''
Input -> An array of integers.
Output -> An array of integers with all the zeroes to the right

Ex:
input -> move_all_zeroes_to_right([0,6,2,0,0,1,0])
ouput -> [1, 6, 2, 0, 0, 0, 0]
'''
def swap(array, pointer_one, pointer_two):
    array[pointer_one], array[pointer_two] = array[pointer_two], array[pointer_one]

def move_all_zeroes_to_right(a):
    low = 0
    high = len(a) -1

    while low < high:
        if a[low] == 0:
            swap(a, low, high)
            if a[low] == 0:
                high -= 1
                swap(a, low, high)
            low += 1
        else:
            if a[high] == 0:
                high -= 1
            low += 1
    return a

test = move_all_zeroes_to_right([0,6,2,0,0,1,0])
print(test)