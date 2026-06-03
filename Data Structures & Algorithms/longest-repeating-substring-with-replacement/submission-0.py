class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap ={}
        l = 0
        r = 0
        n = len(s)
        maxfreq = 0
        maxlen = 0
        while r  < n:
            if s[r] in hashmap:
                hashmap[s[r]] += 1
                
            else:
                hashmap[s[r]] = 1
            maxfreq = max(maxfreq, max(hashmap.values()))
            if (r-l+1) - maxfreq > k:
                hashmap[s[l]] -= 1
                l += 1
                
            if (r-l+1) - maxfreq <= k:
               
                maxlen = max(maxlen, r - l + 1)
                r += 1

        return maxlen

        
                
