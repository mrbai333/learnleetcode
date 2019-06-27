# 06/27/19
# 使用最大堆进行求解
# 1.最大堆的root永远是最小的值，所以每次压栈后检查最大堆的大小即可
# 2.只要大小大于所要求数字，即可将最上面的数字弹出即可
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heapq.heappop(heap)
            