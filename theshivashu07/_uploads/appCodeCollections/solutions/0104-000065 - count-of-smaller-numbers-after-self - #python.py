

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res, seen = [], []
        for num in nums[::-1]:
            idx = bisect.bisect_left(seen, num)
            res.append(idx)
            seen.insert(idx, num)        
        return res[::-1]

