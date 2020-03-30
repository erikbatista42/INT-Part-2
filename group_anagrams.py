# Group anagrams:
# Given an array of strings, group anagrams together.

'''
Input -> Array of Strings
Output -> Array of Arrays of strings

Ex:
input -> groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
ouput -> [
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

def groupAnagrams(strs):
    result = []
    table = {}
    
    for string in strs:
        sorted_string = sorted(string)
        sorted_string = "".join(sorted_string) # turn list into string
        if sorted_string not in table:
            # have the value be the sorted string so we can check if it's an anagram
            initial_list = [string]
            table[sorted_string] = initial_list
        else:
            table[sorted_string].append(string)
    
    for value in table.values():
        # since the values are lists, we want to add each list to the result array
        result.append(value)
    
    return result

a = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(a)