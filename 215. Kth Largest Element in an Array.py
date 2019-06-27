 Date : 06/27/19
# 使用快排进行排序
# 1.每次取比pivot大的值放在列表前面，比pivot小的值放在pivot后面
# 2.当索引位置位k-1时，则前面都是比它大的，即可停止返回
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while low <= high:
            pivot = self.partition(nums, low, high)
            if pivot == k-1:
                return nums[pivot]
            if pivot < k-1:
                low = pivot + 1
            else:
                high = pivot - 1
        
    def partition(self, nums, low, high):
        pivot_value = nums[high]
        index = low
        for i in range(low, high):
            if nums[i] >= pivot_value:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        nums[index], nums[high] = nums[high], nums[index]
        return index