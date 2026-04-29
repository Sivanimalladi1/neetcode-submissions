class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        len1 = len(s)
        len2 = len(t)
        if len1 == len2:
            for i in s:
                count1 = s.count(i)
                count2 = t.count(i)
                if count1 != count2:
                    return False
            return True
        else:
            return False

        
        