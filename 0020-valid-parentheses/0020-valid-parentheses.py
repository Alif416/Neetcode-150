from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = deque()

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False

                e = stack.pop()

                if my_dict[ch] != e:
                    return False

        return len(stack) == 0