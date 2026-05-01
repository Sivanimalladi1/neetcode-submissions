class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        ans = [] 
        sorted_by_values = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
        print(sorted_by_values)
        for val, count in sorted_by_values.items():
            if k != 0:             
                ans.append(val)
                k -= 1
            else:
                break

        return ans

       






        