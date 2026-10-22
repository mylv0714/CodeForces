
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rq = deque()
        dq = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                rq.append(i)
            else:
                dq.append(i)

        while rq and dq:
            r = rq.popleft()
            d = dq.popleft()

            if r < d: # Radiant가 먼저나옴
                rq.append(r + n)
            else:
                dq.append(d + n)

        return "Radiant" if rq else "Dire"