# 06/27/19
# 使用字典进行求解
# 1.遍历列表的值，将列表的值和位号存入字典，查找字典中的值并返回位号即可
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        tsum = {}
        for i,v in enumerate(numbers):
            if target - v in tsum:
                result.append(tsum[target - v]+1)
                result.append(i+1)
                return result
            else:
                tsum[v] = i