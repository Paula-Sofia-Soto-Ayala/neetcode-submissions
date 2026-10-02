class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for index,num in enumerate(nums):
            complement = target - num
            if complement in dic:
                return [dic[complement], index]
            if num not in dic:
                dic[num] = index