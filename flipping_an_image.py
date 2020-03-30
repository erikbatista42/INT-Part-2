# Flipping an image

'''
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Input -> Array of arrays of Ints
Output -> Array of arrays of Ints

Ex:
input -> flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
ouput -> [[1,0,0],[0,1,0],[1,1,1]]
'''

def swap(array, pointer_one, pointer_two):
    array[pointer_one], array[pointer_two] = array[pointer_two], array[pointer_one]
        
def flip(array):
    '''Reverse the array'''
    start = 0
    end = len(array) -1
    while start < end:
        swap(array, start, end)
        start += 1
        end -= 1
    
def invert(array):
    '''Each 0 is replaced by one and each 1 is replace by 0''' 
    for index, value in enumerate(array):
        if array[index] == 0:
            array[index] = 1
        else:
            array[index] = 0 
            
def flipAndInvertImage(a):
    for index, val in enumerate(a):
        flip(a[index])
        invert(a[index])
    return a

test = flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
print(test)