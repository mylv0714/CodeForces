class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        read = write = 0

        while read < n:
            ch = chars[read]
            cnt = 0
            while read < len(chars) and chars[read] == ch:
                read += 1
                cnt += 1

            chars[write] = ch
            write += 1
          
            if cnt > 1:
                for s in str(cnt):
                    chars[write] = s
                    write += 1

        return write
