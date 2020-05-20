import unittest
from index import minimum_jump

class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(minimum_jump([1, 2]), 1)
    def test_2(self):
        self.assertEqual(minimum_jump([2, 3, 1, 1, 4]), 2)
    def test_3(self):
        self.assertEqual(minimum_jump([0]), 0)
    def test_4(self):
        self.assertEqual(minimum_jump([3,2,1]), 1)
    def test_5(self):
        self.assertEqual(minimum_jump([2, 3, 1]), 1)
    def test_6(self):
        self.assertEqual(minimum_jump([3, 5, 1, 1, 1, 1]), 2)
    def test_7(self):
        self.assertEqual(minimum_jump([1,0]), 1)
    def test_8(self):
        self.assertEqual(minimum_jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]), 2)

# print(minimum_jump([1, 2]))  # 1
# print(minimum_jump([2, 3, 1, 1, 4]))  # 2
# print(minimum_jump([0]))  # 0
# print(minimum_jump([3, 2, 1]))  # 1
print(minimum_jump([2, 3, 1]))  # 1
# print(minimum_jump([3, 5, 1, 1, 1, 1]))  # 2
# print(minimum_jump([1,0]))  # 1

if __name__ == '__main__':
    unittest.main()



# class Solution:
#     def numberOfArrays(self, s: str, k: int) -> int:
#         k_length = len(str(k))
#         nums = self.get_numbers(s)
#         for num in nums:
#             if

#     def get_numbers(self, s: str, k: int):
#         output = []
#         n = len(s)
#         for i in range(n):
#             for length in range(i+1, n+1):
#                 num = int(s[i: length])
#                 if 1 <= num and num <= k:
#                     output.append(num)
#         return output


#     def is_valid(self, inputs : List[str] ):
#         for num in inputs:


# print(Solution().numberOfArrays(s="1317", k=2000))


# with open('input01.txt', 'r') as file:
#     input_lines = [line.strip() for line in file]
#     n, d = map(int, input_lines[0].split())
#     expenditure = list(map(int, input_lines[1].split()))


#     result = activityNotifications(expenditure, d)

#     print(str(result) + '\n')
