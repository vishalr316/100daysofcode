# Solution for - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        original_heights = list.copy(heights)
        heights.sort(reverse=True)
        res = []

        for i in range(len(names)):
            ind = original_heights.index(heights[i])
            res.append(names[ind])
        return res
