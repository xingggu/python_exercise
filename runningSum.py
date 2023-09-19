class Solution:
    """
    考虑数组正负index
    """

    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums