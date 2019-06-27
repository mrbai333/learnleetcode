# Date : 06/27/19
# 1.使用位运算进行判断，i & (i-1)是去掉n的二进制位中最后一位的1
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = range(num+1)
        count = 0
        result[0] = 0
        for i in range(1,num+1):
            result[i] = result[i&(i-1)] + 1
        return result
            