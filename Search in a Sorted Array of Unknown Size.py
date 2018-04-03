class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        low, high = 0, 1
        def binarySearch(reader, target, low, high):
            while high >= low:
                mid = low + (high-low) // 2
                print(low, mid, high)
                if reader.get(mid) == target:
                    return mid
                if reader.get(mid) > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1
        while reader.get(high) < target:
            low = high
            high *= 2
        return binarySearch(reader, target, low, high)
