class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        answer = []  

        for i in range(len(nums) - k + 1):
            group = nums[i:i+k]    
            biggest = max(group)    
            answer.append(biggest)  
        return answer
