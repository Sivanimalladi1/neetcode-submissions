class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += f"{len(s)}#{s}"
        return encode

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        ans = 0
        while i < len(s):
            length = 0
            while s[i] != '#':
                length = length * 10 + (ord(s[i]) - ord('0'))
                i += 1
            i += 1

            ans = s[i: i + length]
            res.append(ans)

            i += length
        
        return res



