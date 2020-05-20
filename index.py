from typing import List, Dict
import random
import numpy
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

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr = []
        potential_str = ''
        for c in s2:
            if c in s1:
                potential_str += c
            else:
                if len(s1) <= len(potential_str):
                    arr.append(potential_str)
                potential_str = ''
                
        if len(s1) <= len(potential_str):
            arr.append(potential_str)
        if not arr:
            return False
        
        d1 = collections.Counter(s1)
        
        print(arr)
        for e in arr:
            d = collections.Counter(e)
            for key in d:
                if key not in d1 or d[key] < d1[key]:
                    return False

        return True
                


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dic = {}
        for i, c in enumerate(cost):
            dic[c] = i + 1
        print(dic)
        sets = list(set(cost))
        print(sets, target)

        # def coinChange(coins, amount) -> int:
        #     dp = [float('inf')] * (amount + 1)
        #     dp[0] = 0

        #     for coin in coins:
        #         for x in range(coin, amount + 1):
        #             dp[x] = min(dp[x], dp[x - coin] + 1)
        #     return dp[amount] if dp[amount] != float('inf') else -1
        # answer = coinChange(sets, target)
        # print(answer)

        def coinChange(idxCoin, coins, amount):
            if amount == 0:
                return [0, None]
            if idxCoin < len(coins) and amount > 0:
                maxVal = amount//coins[idxCoin]
                maxCost = float('-inf')
                for x in range(maxVal + 1):

                    if amount >= x * coins[idxCoin]:

                        res = coinChange(idxCoin + 1, coins,
                                         amount - x * coins[idxCoin])
                        if (res[0] != -1):
                            if maxCost < res[0] + x:
                                maxCost = res[0] + x

                if maxCost != float('-inf'):
                    print(maxCost)

                return [-1, None] if maxCost == float('-inf') else [maxCost, None]
            return [-1, None]
        a = coinChange(0, sets, target)
        print(a)


print(Solution().largestNumber(cost=[4, 3, 2, 5, 6, 7, 2, 5, 5], target=9))
print(Solution().largestNumber(cost=[7, 6, 5, 5, 5, 6, 8, 7, 8], target=12))
print(Solution().largestNumber(cost=[2, 4, 6, 2, 4, 6, 4, 4, 4], target=5))
print(Solution().largestNumber(
    cost=[6, 10, 15, 40, 40, 40, 40, 40, 40], target=47))


# def permute2(self, nums: List[int], index: int, output: List[List[int]]) -> List[List[int]]:
#     if index == len(nums):
#         return output
#     for num in nums:
#         for collection in output:
#             collection = collection + [num]

#     return self.permute2(nums = nums, index= index + 1, output = output)


# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         score = 0
#         for i in range(k):
#             if sum(cardPoints[-(k-i):]) < sum(cardPoints[:k-i]):
#                 score += cardPoints[0]
#                 del cardPoints[0]
#             else:
#                 score += cardPoints[-1]
#                 del cardPoints[-1]

#         return score


# print(Solution().maxScore([1,2,3,4,5,6,1], 3))
# print(Solution().maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7))
# print(Solution().maxScore( cardPoints = [1,79,80,1,1,1,200,1], k = 3))
# print(Solution().maxScore( [11,49,100,20,86,29,72], 4))


# def reverseShuffleMerge(s):
#     dic = {}
#     print(s)
#     for i in s:
#         if i not in dic:
#             dic[i] = 1
#         else:
#             dic[i] += 1
#     output = ""
#     for key in dic:
#         output += key * (dic[key] // 2)

#     ss = "".join(sorted(output))
#     rss = "".join(reversed(ss))
#     print(rss)
#     i = 1
#     while rss not in s:
#         ss = ss[i:] + ss[:i]
#         print("".join(ss))
#         rss = "".join(reversed(ss))
#         print(rss)
#         i += 1
#     return ss


# print(reverseShuffleMerge("abcdefgabcdefg"))

# # A O(n^2) Python3 program for construction of BST from preorder traversal

# # A binary tree node
# class Node():

#     # A constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# # constructTreeUtil.preIndex is a static variable of
# # function constructTreeUtil

# # Function to get the value of static variable
# # constructTreeUtil.preIndex
# def getPreIndex():
#     return constructTreeUtil.preIndex

# # Function to increment the value of static variable
# # constructTreeUtil.preIndex
# def incrementPreIndex():
#     constructTreeUtil.preIndex += 1

# # A recurseive function to construct Full from pre[].
# # preIndex is used to keep track of index in pre[[].
# def constructTreeUtil(pre, low, high, size):

#     # Base Case
#     if( getPreIndex() >= size or low > high):
#         return None

#     # The first node in preorder traversal is root. So take
#     # the node at preIndex from pre[] and make it root,
#     # and increment preIndex
#     root = Node(pre[getPreIndex()])
#     incrementPreIndex()

#     # If the current subarray has onlye one element,
#     # no need to recur
#     if low == high :
#         return root

#     # Search for the first element greater than root
#     for i in range(low, high+1):
#         if (pre[i] > root.data):
#             break

#     # Use the index of element found in preorder to divide
#     # preorder array in two parts. Left subtree and right
#     # subtree
#     root.left = constructTreeUtil(pre, getPreIndex(),  i-1 , size)

#     root.right = constructTreeUtil(pre, i, high, size)

#     return root

# # The main function to construct BST from given preorder
# # traversal. This function mailny uses constructTreeUtil()
# def constructTree(pre):
#     size = len(pre)
#     constructTreeUtil.preIndex = 0
#     return constructTreeUtil(pre, 0, size-1, size)


# def printInorder(root):
#     if root is None:
#         return
#     printInorder(root.left)
#     print(root.data)
#     printInorder(root.right)


# # Driver program to test above function
# pre = [10, 5, 1, 7, 40, 50]

# root = constructTree(pre)
# print("Inorder traversal of the constructed tree:")
# printInorder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
