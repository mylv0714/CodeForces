class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                stack.append((cur, num))
                cur = ""
                num = 0

            elif ch == ']':
                prev_str, repeat = stack.pop()
                cur = prev_str + cur * repeat

            else:
                cur += ch

        return cur