# I did this one because i was curious what the actual problem was
# the answer is that a simple iterative approach wasn't fast enough

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if (n == 0):
            return 1

        if (n < 0):
            n = n * -1
            x = 1 / x

        if (n % 2 == 0):
            return self.myPow(x * x, int(n / 2))
        else:
            return x * self.myPow(x * x, int((n - 1) / 2))

sol = Solution()
print(sol.myPow(3, 2))