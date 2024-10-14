def lengthOfLongestSubstring(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1
    #Keep track of left and total_substrings
    left = longest_substrings = 0
    # Create Set
    seen = set()
    #Start a for loop that iterates once in the string var: right
    for right in range(len(s)):
        #yes -> while loop that decrease pops the left value from set until its gone. 
        #Also increase left value by 1 
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        #no -> we add the value in set and continue to next iteration
        seen.add(s[right])
        curr_length = right - left + 1
        longest_substrings = max(curr_length,longest_substrings)
    return longest_substrings

print(lengthOfLongestSubstring("s")) # 3