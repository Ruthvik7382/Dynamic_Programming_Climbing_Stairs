#!/usr/bin/env python
# coding: utf-8

# In[32]:


class Solution(object):
    def climbStairs(self, n, memo={}):
        """
        :type n: int
        :rtype: int
        """
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        elif n < 0:
            return 0
        else:
            ways = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
            memo[n] = ways
            return ways

solution_instance = Solution()
result = solution_instance.climbStairs(5)
print(f"Number of combinations for n=5: {result}")

