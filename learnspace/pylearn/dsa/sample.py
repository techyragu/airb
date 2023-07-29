# l1 = ["aaa", "ab", "c"]
# l2 = sorted(l1, key=lambda l: len(l))
# print(l2)

# def my_decorator(func):
#     def wrapper():       
#         num= int(func())
#         return num *2
#     return wrapper

# @my_decorator
# def number():
#     return "123"

# print(number())

# class Solution:
#     def missingNumber(self, nums):
#         nb = len(nums) + 1
#         nums.append(nb)
#         i = 0
#         while i < len(nums):
#             print(nums)
#             j = nums[i]
#             if nums[i] != nb and j != nb and nums[i] != nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]
#             else:
#                 i += 1
                
#             for i in range(len(nums)):
#                 if nums[i] != i:
#                     return i
                
# s = Solution()
# print(s.missingNumber([3,0,1]))


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# stack = [(TreeNode(), None)]
# a, b = stack.pop()
# print(a, b)

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        print(A)
        if A//10 == 0:
            return 1 if A%10 == 1 else 0

        return self.solve(self.sd(A))

    def sd(self, N):
        print(N)
        if N//10 == 0:
            return N%10
        return self.sd(N//10) + N%10
    
s = Solution()
print(s.solve(83557))
#print(s.sd(83557))
