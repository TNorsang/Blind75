class Solution:
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


problem = Solution()

list_of_word1 = ["","a","","abc","abcdefghijklmnopqrstuvwxy","z"]
list_of_word2 = ["","","b","def","z","abcdefghijklmnopqrstuvwxy"]
for i in range(len(list_of_word1)):
    ans = problem.merge_string_alternately(list_of_word1[i],list_of_word2[i])
    print(f"Input : Word1: {list_of_word1[i]}, Word2: {list_of_word2[i]} | Output : {ans} ")

