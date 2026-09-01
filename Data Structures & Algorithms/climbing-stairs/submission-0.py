class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * (n+1)
        ways[0],ways[1] = 1,1
        i = 2
        if n == 0:
            return n
        elif n == 1:
            return n
        else:
            while i<=n:
                ways[i] = ways[i-1] + ways[i-2]
                i+=1
            return ways[n]