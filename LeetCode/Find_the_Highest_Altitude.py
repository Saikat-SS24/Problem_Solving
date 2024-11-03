class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        height = 0
        for i in gain:
            height += i
            res = max(res,height)
        return res
