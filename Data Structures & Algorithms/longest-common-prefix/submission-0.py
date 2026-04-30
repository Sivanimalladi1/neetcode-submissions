class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        v = sorted(strs)
        firstStr = v[0]
        lastStr = v[-1]
        ans = ""

        for ind in range(min(len(firstStr), len(lastStr))):
            if(firstStr[ind] != lastStr[ind]):
                return ans
            ans += firstStr[ind]
        return ans
        

        