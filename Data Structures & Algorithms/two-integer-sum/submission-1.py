class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mp={}

        for i in range(0,len(nums)):
            if target-nums[i] in mp:
                return [mp.get(target-nums[i]),i]
            # if nums[i] in mp: continue
            mp[nums[i]]=i
        return [0,0]
        