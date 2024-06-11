# Solution for - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        diff = []
        points.sort()
        for i in range(len(points)-1):
            diff.append(abs(points[i][0] - points[i+1][0]))
        return max(diff)
