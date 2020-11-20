#Data Structure: Lists
#Algorithm: Sorting and iteration

"""Notes:
    Sort
    Iterate through and create the answer arrays by comparing the end value to the current first value
    
Brute Force pseudo code:
    -Sort
    -Initialize Answer = []
    -Initialize prev_start as arr[0][0]
    -Initialize prev_end as arr[0][1]
    -Iterate
        -Start on second element
        -curr_start = curr_arr[0]
        -curr_end = curr_arr[1]
        -if curr_start > prev_end (moving to the next interval):
            Answer.append([prev_start, prev_end])
            prev_start = curr_start
            prev_end = curr_end
        else: (merge)
            prev_end = max(prev_end, curr_end)
    (adds the last part to the answer, since it will end without appending in both cases)
    Answer.append([prevstart, prev_end])
        
Time Complexity: 2nlogn -> nlogn
Space Complexity: O(n) - n being the size of the intervals array

Interval questions usually require a sort.
Typically, you will need to compare the previous end value and the current first value
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: (x[0], x[1]))
        answer = []
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        for i in range(1,len(intervals)):
            curr_start, curr_end = intervals[i]
            if curr_start > prev_end:
                answer.append([prev_start, prev_end])
                prev_start = curr_start
                prev_end = curr_end
            else:
                prev_end = max(prev_end, curr_end)
        answer.append([prev_start, prev_end])
        return answer