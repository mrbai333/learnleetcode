# 06/27/19
# 使用字典进行遍历
# 1.由于heapq默认是最小堆，代码中在堆的push时给权重加了负号，
# 2.这样堆顶部对应的实际上是出现次数最多的数
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        data, res, pq = {}, [], []
        for i in nums:
            data[i] = data[i] + 1 if i in data else 1
        for key in data:
            heapq.heappush(pq,(-data[key],key))
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        return res