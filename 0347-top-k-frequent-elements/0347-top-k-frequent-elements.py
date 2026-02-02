from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0: return []
        count = Counter(nums)
        k_max = min(k, len(count))
        return heapq.nlargest(k_max, count.keys(), key=count.get)
        