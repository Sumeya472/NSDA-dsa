class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0          
        letters = []       

        for letter in s:
            while letter in letters:
                letters.pop(0)

            letters.append(letter)

            if len(letters) > count:
                count = len(letters)

        return count
