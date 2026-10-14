class Solution:
    memo = [0]*38 # 0<=n<=37
    memo[0],memo[1], memo[2] = 0,1,1
    def tribonacci(self, n: int) -> int:
        if n <=2 : return self.memo[n]
        if self.memo[n] > 0 :
            return self.memo[n]
        else:
            self.memo[n] = self.tribonacci(n-1)+ self.tribonacci(n-2) + self.tribonacci(n-3)
            return self.memo[n]

#print(Solution().tribonacci(25))