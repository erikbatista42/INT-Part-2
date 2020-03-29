# Generate Binary Numbers from 1 to n using a Queue

# Implement a function findBin(n) which will generate binary numbers from 11 
# till nn in the form of a string using a queue. The myQueue() and myStack() 
# classes are provided in all of these challenges. 

'''
Input -> A positive integer nn
Output -> Returns binary numbers in the form of strings from 1 up to n

Ex:
findBin(n: 3)

-> ["1","10","11"]
'''
import queue
def findBin(n):
    '''
    Time + Space: O(n) - because the list is iterated over once 
    '''
    result = []
    q = queue.Queue()
    q.put(1)
    for i in range(n):
        result.append(str(q.get()))
        s1 = result[i] + "0"
        s2 = result[i] + "1"
        q.put(s1)
        q.put(s2)

    return result

print(findBin(3))