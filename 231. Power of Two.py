# Date : 06/27/19
# 1.使用位运算进行判断，n & (n-1)是去掉n的二进制位中最后一位的1
# 2.如果是2的幂，则二进制中应只有1位是1
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not n&(n-1)