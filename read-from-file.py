import csv
import json
import collections
import os

# with open('data.json') as f:
#     data = json.load(f)
#     print(data)


def maxSubsetSum(arr, memo={}):
    n = len(arr)
    if len(arr) == 0:
        return 0
    key = tuple(arr)
    if key in memo:
        return memo[key]
    maximum = 0
    for i in range(len(arr)):
        j = 0 if i < 1 else i-1
        newArr = arr[:j] + arr[i+2:]
        maximum = max(maximum, maxSubsetSum(newArr, memo),
                      maxSubsetSum(newArr, memo) + arr[i])
    memo[key] = maximum
    return maximum

arr = []
with open("input.txt") as f:
    c = csv.reader(f, delimiter=' ', skipinitialspace=True)
    for line in c:
        arr = line[:]

print(maxSubsetSum(arr))