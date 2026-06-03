class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        hashmap = {}
        count = 0
        tlen = len(t)
        l = 0
        r = 0
        sindex = -1
        minval = pow(10, 9)
        n = len(s)
        for i in t:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        #print(hashmap)
        while r < n:
            if s[r] in hashmap:
                if hashmap[s[r]] > 0:
                    count += 1
                hashmap[s[r]] -= 1
            else:
                hashmap[s[r]] = -1
            
            while count == tlen:
                if r - l + 1 < minval:
                    minval = r-l + 1
                    sindex = l
                
                if s[l] in hashmap:
                    hashmap[s[l]] += 1
                    if hashmap[s[l]] > 0:
                        count -= 1

                    l += 1
            r += 1
        if sindex == -1:
            return res
        return res + s[sindex : sindex+minval]

        
