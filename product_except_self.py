'''
Input -> Array of Integers
Output -> Array of Integers 

Ex:
input -> products([1, 2, 3, 4, 5])
ouput -> [0, 0, 1, 1, 1, 1, 2, 2]
'''
def products(a):
    temp = 1
    # generate prefix nums (we do this using a running multiplier)
    prefix = []
    for num in a:
        temp *= num
        prefix.append(temp)

    temp = 1 # reset 

    # generate suffix nums (we do a running multiplier but this time in reversed)
    suffix = []
    for num in reversed(a):
        temp *= num 
        suffix.append(temp)
    
    suffix = list(reversed(suffix)) # reverse again

    # generate result using prefix & suffix
    result = []
    for i in range(len(a)):
        if i == 0:
            result.append(suffix[i + 1])
        elif i == len(a)-1:
            result.append(prefix[i-1])
        else:
            result.append(prefix[i-1] * suffix[i+1])

    return result

print(products([1, 2, 3, 4, 5]))