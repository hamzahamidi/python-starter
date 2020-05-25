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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(' ')
        for i, w in enumerate(sentence):
            if w.startswith(searchWord):
                return i + 1
        return -1

    def maxVowels(self, s: str, k: int) -> int:
        vowel = 'aeiou'
        max_counter = 0
        queue = []
        for i in range(len(s)):

            if s[i] in vowel:
                queue.append(i)

            if queue and k <= i - queue[0]:
                queue.pop(0)
            max_counter = max(max_counter, len(queue))
        return max_counter

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:

        def dfs(tree, arr=[]):
            if tree is None:
                return [arr]

            new_arr = arr + [tree.val]

            if tree.left is None and tree.right is None:
                return [new_arr]

            left = [] if tree.left is None else dfs(tree.left, new_arr)
            right = [] if tree.right is None else dfs(tree.right, new_arr)

            return left + right

        arr = dfs(root)
        answer = 0
        for e in arr:
            d = collections.Counter(e)
            counter = 0
            for key in d:
                if d[key] % 2 == 1:
                    counter += 1
            
            if counter <= 1:
                answer += 1

        return answer

    # Failed need to try it again
    def maxDotProduct(self, nums1, nums2) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0 for i in range(m + 1)]  
                for j in range(n + 1)] 
    
        for i in range(1, n + 1, 1): 
            

            for j in range(i, m + 1, 1): 

                dp[i][j] = max((dp[i - 1][j - 1] + 
                                (nums1[j - 1] * nums2[i - 1])) ,  
                                dp[i][j - 1]) 
    
        return dp[n][m]




print(Solution().maxDotProduct([2,1,-2],  [3,0,-6]))
print(Solution().maxDotProduct(nums1 = [-1,-1], nums2 = [1,1]))

# Tree = TreeNode(2)
# Tree.left = TreeNode(3)
# Tree.right = TreeNode(1)
# Tree.left.left = TreeNode(3)
# Tree.left.right = TreeNode(1)
# Tree.right.right = TreeNode(1)

# print(Solution().pseudoPalindromicPaths(Tree))


# print(Solution().maxVowels(s="abciiidef", k=3))
# print(Solution().maxVowels(s="aeiou", k=2))
# print(Solution().maxVowels(s="leetcode", k=3))
# print(Solution().maxVowels(s="rhythms", k=4))
# print(Solution().maxVowels(s="tryhard", k=4))
# print(Solution().maxVowels(s="weallloveyou", k=7))

# print(Solution().isPrefixOfWord(sentence="i am tired", searchWord="you"))

