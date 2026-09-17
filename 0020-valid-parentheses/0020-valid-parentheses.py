class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif ch in ')}]':
                if not stack:
                    return False

                e = stack.pop()
                if e != hashmap[ch]:
                    return False

        return not stack