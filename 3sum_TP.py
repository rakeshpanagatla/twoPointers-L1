class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        i = 0
        while(i < len(nums)-2):
            l = i+1
            r = len(nums)-1
            while(l < r):
                
                sum = nums[i]+nums[l]+nums[r]
                if (sum == 0):
                    triplet = []
                    triplet.append(nums[i])
                    triplet.append(nums[l])
                    triplet.append(nums[r])
                    answer.append(triplet)
                    while(l < r and nums[l] == nums[l+1] ):
                        l += 1
                    while(l < r and nums[r] == nums[r-1]):
                        r -= 1
                    
                    l += 1
                    r -= 1
                elif(sum < 0):
                    l += 1
                else:
                    r -=1
            while(i<len(nums)-2 and nums[i] == nums[i+1] ):
                i += 1
            i += 1  
        return answer