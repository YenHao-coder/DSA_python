import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) < k : return float('-inf')
        nums_k = nums[:k]
        heapq.heapify(nums_k)
        for e in nums[k:]:
            if e > nums_k[0]: heapq.heapreplace(nums_k, e)
        return nums_k[0]