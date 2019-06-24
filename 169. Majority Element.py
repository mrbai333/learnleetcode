# Date : 06/24/19
# 使用枚举的方式进行判断
# 1.首先建立字典，枚举列表中的元素，进行计数，将元素和元素的个数作为键值对存放在字典中
# 2.判断字典中的value值，如果有大于列表一半长度的则返回该value值对应的key值
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numdict = {}
        for i,v in enumerate(nums):
            if v in numdict:
                numdict[v] += 1
            else:
                numdict[v] = 1
        for k,v in numdict.items():
            if v >= len(nums) / 2:
                return k