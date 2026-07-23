class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nNums = {}
        for pos in range(len(nums)):
            nNum = target - nums[pos]
            if nums[pos] in nNums:
                return [nNums[nums[pos]], pos]
            else:
                nNums[nNum] = pos