# Number of Valid Words for Each Puzzle

'''
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
word contains the first letter of puzzle.
For each letter in word, that letter is in puzzle.
For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage"; while invalid words are "beefed" (doesn't include "a") and "based" (includes "s" which isn't in the puzzle).
Return an array answer, where answer[i] is the number of words in the given word list words that are valid with respect to the puzzle puzzles[i].

Input: 
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation:
1 valid word for "aboveyz" : "aaaa" 
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There're no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.


Input -> Array of Strings(words), Array of Strings(puzzles), 
Output -> Array of Ints

Ex:
Input -> findNumOfValidWords(words: ["aaaa","asas","able","ability","actt","actor","access"],
    puzzles: ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"])

Output -> [1,1,3,2,4,0]

'''

def findNumOfValidWords(words, puzzles):
    import collections
    import itertools
    count = collections.Counter(frozenset(w) for w in words)
    res = []
    for p in puzzles:
        cur = 0
        for k in range(7):
            for c in itertools.combinations(p[1:], k):
                cur += count[frozenset(tuple(p[0]) + c)]
        res.append(cur)
    return res

a = findNumOfValidWords(["aaaa","asas","able","ability","actt","actor","access"],
["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"])

print(a)