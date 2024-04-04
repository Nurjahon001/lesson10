class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        from math import gcd
        lcm = (2 * n) // gcd(2, n)
        return lcm

solution=Solution()
print(solution.smallestEvenMultiple(5))