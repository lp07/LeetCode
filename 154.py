# 154. Find Minimum in Rotated Sorted Array II
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,4,4,5,6,7] might become:
# [4,5,6,7,0,1,4] if it was rotated 4 times.
# [0,1,4,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], .., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], ., a[n-1]].
# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
# You must decrease the overall operation steps as much as possible
# Example 1:
# Input: nums = [1,3,5], Output: 1
# Example 2:
# Input: nums = [2,2,2,0,1],  Output: 0

class Solution:
    def findMin(self, nums):
        # remove the duplicates
        new_nums = sorted(set(nums))
        low = 0
        high = len(new_nums) - 1
        while low < high:
            mid = (low + high) // 2
            if new_nums[mid] == new_nums[high]:
                high -= 1
            elif new_nums[mid] > new_nums[high]:
                low = mid + 1
            else:
                high = mid
        return new_nums[low]

solution = Solution()
result = solution.findMin([4, 5, 6, 7, 0, 1, 2])
print(result)
