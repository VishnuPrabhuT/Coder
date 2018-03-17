from collections import Counter
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = Counter(words)
        lis = list(counts.items())
        lis.sort(key = lambda item : (-item[1], item[0]))
        return [item[0] for item in lis[:k]]
