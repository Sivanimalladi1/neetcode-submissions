class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = 0
        maxlen = 0
        for i in range(len(s)):
            while s[i] in hashset:
                hashset.remove(s[l])
                l += 1
            
            hashset.add(s[i])
            maxlen = max(maxlen, i -l + 1)

        return maxlen