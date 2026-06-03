class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = 0
        maxlen = 0
        for i in range(len(s)):
            if s[i] in hashmap:
                l = max(hashmap[s[i]] +1, l )
            
            hashmap[s[i]] = i
            maxlen = max(maxlen, i -l + 1)

        return maxlen