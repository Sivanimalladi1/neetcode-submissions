class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1) 
        n2 = len(word2) 
        i = 0
        j = 0
        ans = ""

        while n1 != 0 and n2 != 0:
            ans += word1[i]
            ans += word2[j]
            n1 -= 1
            n2 -= 1
            i += 1
            j += 1
        
        if n1 != 0:
            while n1 != 0:
                ans += word1[i]
                n1 -= 1
                i += 1
            
        if n2 != 0:
            while n2 != 0:
                ans += word2[j]
                n2 -= 1
                j += 1

        return ans