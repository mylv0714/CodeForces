class RecentCounter:
    

    def __init__(self):
        self.rq = []    

    def ping(self, t: int) -> int:
        self.rq.append(t)
        ans = 0
        for r in self.rq:
            if r >= t-3000 and r <= t:
                ans += 1
        return ans


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# r = RecentCounter()
# print(r.ping(1))
# print(r.ping(100))
