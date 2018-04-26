from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bucket = [[] for _ in nums]
        base = collections.defaultdict(int)
        for i in nums:
            base[i] += 1
        for num, freq in base.items():
            bucket[-freq].append(num)
        return list(itertools.chain(*bucket))[:k]
        
        
        
        
        
        
        
        #counts = Counter(nums)
        #lis = list(counts.items())
        #lis.sort(key = lambda element:(-element[1], element[0]))
        #return [item[0] for item in lis[:k]]
