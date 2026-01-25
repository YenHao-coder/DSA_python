class Solution:
    def isValid(self, s: str) -> bool:
        '''驗證有效的括號'''
        Cmap ={")":"(", "]":"[", "}":"{"}
        stack = []
        for char in s:
            if char in Cmap:
                top_char = stack.pop() if stack else "#"
                if Cmap[char] != top_char: return False
            else:
                stack.append(char)

        return not stack