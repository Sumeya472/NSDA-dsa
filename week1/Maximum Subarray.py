class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = ans = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            ans = max(ans, current)

        return ans
