# 1768. Merge String Alternately

[LeetCode Problem Link](https://leetcode.com/problems/merge-strings-alternately/)

## Problem Statement

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

### Examples

#### Example 1:

**Input:** word1 = "abc", word2 = "pqr"  
**Output:** "apbqcr"  
**Explanation:** The merged string will be merged as so:  
word1: a b c  
word2: p q r  
merged: a p b q c r

#### Example 2:

**Input:** word1 = "ab", word2 = "pqrs"  
**Output:** "apbqrs"  
**Explanation:** Notice that as word2 is longer, "rs" is appended to the end.  
word1: a b  
word2: p q r s  
merged: a p b q r s

#### Example 3:

**Input:** word1 = "abcd", word2 = "pq"  
**Output:** "apbqcd"  
**Explanation:** Notice that as word1 is longer, "cd" is appended to the end.  
word1: a b c d  
word2: p q  
merged: a p b q c d

### Constraints

1. 1 <= word1.length, word2.length <= 100
2. word1 and word2 consist of lowercase English letters.

# My Solution and Thought Process

I initially started with wanting to add into an empty string called mergedString.
The solution works well but it is not an optimal method, the reason why is when you append onto a string
in python, since strings are immutable, python has to create a new string each time I add a character to mergedString.
And when I do this for every n characters it adopts a quadratic time complexity since python copies over all the characters
of old string to the new string and then add the new character. Since the input size has a length constraint of being between 1 and 100 this quadratic complexity is less noticeable.

### Code Example:

```
def merge_string_alternately(self,word1,word2):
        if not word1:
            return word2
        elif not word2:
            return word1

        merged_string = ""

        shorter_word = min(len(word1),len(word2))

        for i in range(shorter_word):
            merged_string += word1[i]
            merged_string += word2[i]

        if len(word1) > shorter_word:
            merged_string += word1[shorter_word:]
        elif len(word2) > shorter_word:
            merged_string += word2[shorter_word:]

        return merged_string
```

For a more optimal solution, I think creating a list for for the merged_string and then appending to that is better since it is
O(1) time complexity to append. Overall the time complexity turns into O(n) since the we iterate through the input once, and space complexity
is O(n) as well since the list grows proportion with the input size n.

```
def merge_string_alternately(self,word1,word2):
        '''
        Same thing just change the appending to list style
        '''
        if not word1:
            return word2
        if not word2:
            return word1

        shorter_word = min(len(word1),len(word2))

        mergedString = []

        for i in range(shorter_word):
            mergedString.append(word1[i])
            mergedString.append(word2[i])

        if len(word1) > shorter_word:
            for i in range(shorter_word, len(word1)):
                mergedString.append(word1[i])
        if len(word2) > shorter_word:
            for i in range(shorter_word, len(word2)):
                mergedString.append(word2[i])

        return ("").join(mergedString)
```
