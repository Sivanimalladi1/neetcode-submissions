class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        ans = "".join(c for c in s if c.isalnum())
        j = len(ans) - 1
        
        while i <= j:    
             
            if ans[i].lower() != ans[j].lower():
                return False
            i += 1
            j -= 1
        return True
            