class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        right = len(nums) - 1
        mid = 0
        while (mid <= right):
            if(nums[mid] == 0):
                swap(nums, left, mid)
                left += 1
                mid += 1
            elif (nums[mid] == 2):
                swap(nums, mid, right)
                right -= 1
            else:
                mid += 1
        
def swap(nums, l, r):
    temp = nums[l]
    nums[l] = nums[r]
    nums[r] = temp