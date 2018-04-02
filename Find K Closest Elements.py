class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        low, high = 0, len(arr) - k
        while low < high:
            mid = (low + high) // 2
            #print("x - arr[mid] - ", x - arr[mid], ",arr[mid+k] - x - ", arr[mid+k] - x, ",x - ", x, ",arr[mid]", arr[mid], ",arr[mid+k]", arr[mid+k])
            if x - arr[mid] > arr[mid+k] - x:
                low = mid + 1
            else:
                high = mid
        return arr[low : low+k]
