# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

'''
Input -> Array of Integers(0's & 1's)
Output -> same input array

Ex:
Input: 
    [
     [1,1,1],
     [1,0,1],
     [1,1,1]
    ]
Output: 
    [
     [1,0,1],
     [0,0,0],
     [1,0,1]
    ]
'''

def find_zeroes(arrays):
    # (array_index, cell_index)
    locations = set()

    for arr_index, arr in enumerate(arrays):
        for cell_index, cell in enumerate(arr):
            if cell == 0:
                locations.add((arr_index, cell_index))
    return locations
    
def setZeroes(matrix):
    # find zero locations
    locations = find_zeroes(matrix)

    for tup in locations:
        # update rows
        matrix[tup[0]] = [0] * len(matrix[tup[0]])

    # update columns
    for tup in locations:
        for arr in matrix:
            arr[tup[1]] = 0

arrs = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]

setZeroes(arrs)
print(arrs)