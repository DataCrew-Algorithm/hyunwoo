# 실패하고 책 봤는데 투포인터로는 구현 X
# class Solution(object):
#     def twoSum(self, nums, target):
#         n = len(nums)
#         new_nums =sorted(nums)
#         left = 0
#         right = n - 1
#         sub_lst = []
#         ans_lst = []

#         while left < right:
#             if new_nums[left] + new_nums[right] < target:
#                 left += 1
#             elif new_nums[left] + new_nums[right] > target:
#                 right -= 1
#             elif new_nums[left] + new_nums[right] == target:
#                 sub_lst.append(left)
#                 sub_lst.append(right)
#                 left += 1
        
#         for i in range(len(sub_lst)):
#             if sub_lst[i] == sub_lst[i-1]:
#                 ans = nums.index(new_nums[i], 1)
#             else:
#                 ans = nums.index(new_nums[i])
#                 ans_lst.append(ans)
            

#         return ans_lst

# num = [3, 3]
# target = 6

# sol = Solution()
# ans = sol.twoSum(num, target)
# print(ans)


# =====================================================================

# 3879ms

class Solution(object):
    def twoSum(self, nums, target):
        ans_lst = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans_lst.append(i)
                    ans_lst.append(j)

        return ans_lst

num = [3, 3]
target = 6

sol = Solution()
ans = sol.twoSum(num, target)
print(ans)


# =====================================================================

# 수현님 아이디어로 고친 투포인터
# 61ms

class Solution(object):
    def twoSum(self, nums, target):
        new_nums =sorted(nums)
        left = 0
        right = len(nums) - 1

        while left < right:
            if new_nums[left] + new_nums[right] < target:
                left += 1
            elif new_nums[left] + new_nums[right] > target:
                right -= 1
            else:
                break
        
        if new_nums[left] == new_nums[right]:
            left_ = nums.index(new_nums[left])
            nums[left_] = "*"
            right_ = nums.index(new_nums[right])

        else:
            left_ = nums.index(new_nums[left])
            right_ = nums.index(new_nums[right])


        return [left_, right_]
