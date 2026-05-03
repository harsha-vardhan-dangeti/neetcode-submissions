class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre_arr = [0] * n
        suff_arr = [0] * n
        res = [0] * n

        pre_arr[0] = suff_arr[n-1] = 1

        for i in range(1,n):
            pre_arr[i] = pre_arr[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suff_arr[i] = suff_arr[i+1] * nums[i+1]
        for i in range(0,n):
            res[i] = pre_arr[i] * suff_arr[i]
        return res

        