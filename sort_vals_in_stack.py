# Implement a function called sortStack() which takes a stack and sorts all of 
# its elements in ascending order such that when they are popped and printed, 
# they come out in ascending order. So the element that was pushed last to the 
# stack has to be the smallest.

'''
Input -> A stack of integers.
Output -> The stack with all its elements sorted in descending order.

Ex:
input -> sortStack([23, 60, 12, 42, 4, 97, 2])
ouput -> [97, 60, 42, 23, 12, 4, 2]
'''

def sortStack(stack):
    temp_lst = [stack.pop() for i in range(len(stack))]

    for i in reversed(sorted(temp_lst)):
        stack.append(i)
    return stack

print(sortStack([23, 60, 12, 42, 4, 97, 2]))