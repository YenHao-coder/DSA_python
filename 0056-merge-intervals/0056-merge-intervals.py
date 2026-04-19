class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for curr in intervals[1:]:
            last_end = merged[-1][1]
            curr_start, curr_end = curr[0], curr[1]
            if curr_start <= last_end:
                merged[-1][1] = max(curr_end, last_end)
            else:
                merged.append(curr)
        
        return merged
        