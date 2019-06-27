class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.quick_sort(nums,0,len(nums)-1)
        return nums[k-1]
    def partition(self,nums,l,r):
        pivot = nums[r]
        i = l - 1
        for j in range(l,r):
            if nums[j] > pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i+1
    def quick_sort(self,nums,l,r):
        if l < r:
            pivot_index = self.partition(nums,l,r)
            self.quick_sort(nums,l,pivot_index-1)
            self.quick_sort(nums,pivot_index+1,r)