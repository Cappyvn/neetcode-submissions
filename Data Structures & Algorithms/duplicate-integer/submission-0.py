class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for c in nums:
            if c not in check:
                check.update({c:1})
            else:
                return True
        return False
