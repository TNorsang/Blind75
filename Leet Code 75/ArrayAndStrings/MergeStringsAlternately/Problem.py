class Solution:
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

problem = Solution()

list_of_word1 = ["","a","","abc","abcdefghijklmnopqrstuvwxy","z"]
list_of_word2 = ["","","b","def","z","abcdefghijklmnopqrstuvwxy"]
for i in range(len(list_of_word1)):
    ans = problem.merge_string_alternately(list_of_word1[i],list_of_word2[i])
    print(f"Input : Word1: {list_of_word1[i]}, Word2: {list_of_word2[i]} | Output : {ans} ")
