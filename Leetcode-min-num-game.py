# Solution for - https://leetcode.com/problems/minimum-number-game/


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        alice = bob = None
        res = []
        while len(nums) > 0:
            mini = nums.index(min(nums))
            if len(nums) % 2 == 0:
                alice = nums.pop(mini)
            else:
                bob = nums.pop(mini)
            if alice is not None and bob is not None:
                res.append(bob)
                res.append(alice)
                alice = bob = None
                
        return res
