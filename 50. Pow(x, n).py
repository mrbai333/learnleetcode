# Date : 06/24/19
# 使用递归的方式进行判断
# 1.判断n是否为0，为0则返回1
# 2.判断n是否为负数，为负数则取反然后取倒数
# 3.判断是否为奇数，为奇数则取x * Pow(x,n-1)使得幂为偶数，如果为偶数则递归调用Pow(x*x,n/2)，使用分治方法递归计算
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1/self.myPow(x,-n)
        if n%2:
            return x * self.myPow(x,n-1)
        return self.myPow(x*x,n/2)