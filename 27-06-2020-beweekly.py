from typing import List, Dict
import random
import numpy as np
from functools import cmp_to_key
from statistics import median
import bisect
import math
import os
import random
import re
import sys
from operator import itemgetter, attrgetter
import collections
from fractions import Fraction


import statistics
class Solution:
    def average(self, salary: List[int]) -> float:
        m = min(salary)
        M = max(salary)

        s = list(filter(lambda x: x != m and x != M , salary))

        return statistics.mean(s)


print(Solution().average(salary = [4000,3000,1000,2000]))
print(Solution().average(salary = [1000,2000,3000]))
print(Solution().average(salary = [6000,5000,4000,3000,2000,1000]))
print(Solution().average(salary = [8000,9000,2000,3000,6000,1000]))


#########################################################################

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1,n+1):
            if n % i == 0:
                factors.append(i)

        return factors[k-1] if k <= len(factors) else -1

print(Solution().kthFactor(n = 12, k = 3))
print(Solution().kthFactor(n = 7, k = 2))
print(Solution().kthFactor(n = 4, k = 4))
print(Solution().kthFactor(n = 1, k = 1))
print(Solution().kthFactor(n = 1000, k = 3))


#############################################################################
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros_index = []
        for i, val in enumerate(nums):
            if val == 0:
                zeros_index.append(i)

        if not zeros_index:
            return len(nums) - 1

        zeros_index = [-1] + zeros_index + [len(nums)]


        maximum = 0
        for i in range(2, len(zeros_index)):
            maximum = max(maximum, zeros_index[i] - zeros_index[i - 2] - 2)
        return maximum


print(Solution().longestSubarray(nums=[1, 1, 0, 1]))
print(Solution().longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(Solution().longestSubarray(nums=[1, 1, 1]))
print(Solution().longestSubarray(nums=[1, 1, 0, 0, 1, 1, 1, 0, 1]))
print(Solution().longestSubarray(nums=[0, 0, 0]))


#####################################################################
# NOT WORKING
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:

        e = [0 for i in range(n+1)]
        deg = [0 for i in range(n+1)]
        for x, y in dependencies:
            e[x] = y + e[x]
            deg[y] = deg[y] + 1
        print(deg, e)

        queue = []
        for i in range(1, n):
            if deg[i] == 0:
                queue.append(i)
        print(queue)
        return 0


print(Solution().minNumberOfSemesters(
    n=4, dependencies=[[2, 1], [3, 1], [1, 4]], k=2))

print(Solution().minNumberOfSemesters(n=5, dependencies=[[2, 1], [3, 1], [4, 1], [1, 5]], k=2))
