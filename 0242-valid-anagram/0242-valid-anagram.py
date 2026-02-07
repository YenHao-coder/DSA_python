from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''驗證是否為異位詞'''
        if len(s) != len(t): return False #邊界條件檢查
        #選擇索引模型 
        count_s = Counter(s)
        #執行抵消/校驗操作
        for c in t:
            if c in count_s and count_s[c] > 0:
                count_s[c] -= 1
            else: return False
            if count_s[c] == 0: del count_s[c]
        #最終一致性檢查
        return len(count_s) == 0
