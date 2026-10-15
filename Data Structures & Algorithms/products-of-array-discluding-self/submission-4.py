class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        suf = [0] * n
        res = [0] * n
        # nums = [1,2,3,4]

        # [1,0,0,0] [0,0,0,1]
        pre[0] = suf[n-1] = 1

        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = pre[i] * suf[i]
        return res