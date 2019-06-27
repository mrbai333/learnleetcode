Date : 06/27/19
# 使用快排进行排序
# 1.每次取比pivot大的值放在列表前面，比pivot小的值放在pivot后面
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums,0,len(nums)-1)
        return nums
    def quick_sort(self,nums,l,r):
        if l < r:
            pivot_index = self.partition(nums,l,r)
            self.quick_sort(nums,l,pivot_index-1)
            self.quick_sort(nums,pivot_index+1,r)
    def partition(self,nums,l,r):
        i = l - 1
        index = nums[r]
        for j in range(l,r):
            if nums[j] < index:
                i = i + 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i+1