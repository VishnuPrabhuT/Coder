class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        base = collections.defaultdict(list)
        for word in words:
            for i in range(len(word)):
                base[word[:i]].append(word)
        #print(base.items())
        def helper(square):
            if len(square) == len(words[0]):
                squares.append(square)
                return
            for word in base[''.join(zip(*square)[len(square)])]:
                #print(base[''.join(zip(*square)[len(square)])], ''.join(zip(*square)[len(square)]), word, square)
                helper(square+[word])
        squares = []
        for word in words:
            #print(squares)
            helper([word])
        return squares
