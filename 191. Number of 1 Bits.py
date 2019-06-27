# Date : 06/27/19
# 1.使用位运算进行计数，n = n & (n-1)是去掉n的二进制位中最后一位的1
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            count = count + 1
            n = n & (n-1)
        return count