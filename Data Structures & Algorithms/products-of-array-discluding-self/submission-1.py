class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # compute prefix array
        # compute suffix array
        # [1, 2, 3, 4]

        # multiply the indicies for result

        n = len(nums)
        pre = [0] * n
        suf = [0] * n
        res = [0] * n

        pre[0] = suf[-1] = 1

        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
             suf[i] = suf[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = pre[i] * suf[i]
        return res
        