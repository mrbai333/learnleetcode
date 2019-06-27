Date : 06/27/19
# 使用快排进行排序
# 1.每次取比pivot大的值放在列表前面，比pivot小的值放在pivot后面
# 2.系统内置函数速度比自己写的快排算法快
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        def quick_sort(nums,l,r):
            if l<r:
                pivot_index = partition(nums,l,r)
                quick_sort(nums,l,pivot_index-1)
                quick_sort(nums,pivot_index+1,r)
        def partition(nums,l,r):
            i = l-1
            index = nums[r]
            for j in range(l,r):
                if nums[j] <= index:
                    i = i + 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[r], nums[i+1] = nums[i+1], nums[r]
            return i+1
        quick_sort(g,0,len(g)-1)
        quick_sort(s,0,len(s)-1)
        # g.sort()
        # s.sort()
        child = 0
        cookies = 0
        while child < len(g) and cookies < len(s):
            if g[child] <= s[cookies]:
                child += 1
            cookies += 1
        return child