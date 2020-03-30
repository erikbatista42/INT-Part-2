# Given a sentence, reverse the words of the sentence. For example, "i live in a house" becomes "house a in live i".

'''
Input -> String
Output -> String 

Ex:
input -> "i live in a house"
ouput -> "house a in live i"
'''
def reverse(string):
    split = string.split()
    result = []
    for item in split:
        result.insert(0, item)
    return  " ".join(result)
    
a = reverse("i live in a house")
print(a)