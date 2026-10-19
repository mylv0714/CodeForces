import heapq

class SmallestInfiniteSet:

    def __init__(self):
        hq = []
        isinstance = set()
        cur = 0

    def popSmallest(self) -> int:
        pass

    def addBack(self, num: int) -> None:
        pass
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

hq = {}
heapq.heappush(hq,3)
heapq.heappush(hq,3)
print(hq)