class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        res = []

        for n in nums:
            counts[n] += 1
        counts = sorted(counts, key=counts.get, reverse=True)

        for i in range(k):
            res.append(counts[i])
        return res
   
        