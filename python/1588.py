class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total_length = len(arr)
        arr_sum = 0
        for t in arr:
            arr_sum += t
            
        for i in range(3, total_length+1, 2):
            for j in range(0, total_length):
                start = j
                end = j + i
                if end <= total_length:
                    arr_sum += sum(arr[start: end])
        
        return arr_sum
