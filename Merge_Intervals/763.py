"""
Notes:
    -Initially looking at the problem, thought of a dictionary
            -Key -> letter
            -Value -> array of indices
    -Intervals cannot overlap so we would merge them
Pseudo Code:
    -loop through the input and create a dictionary with key as the letter
        -collections.defaultdict(list)
        -initialize value as first found idx
        -if the letter is in dictionary then replace the second element of the value
    -Sort the dictionary values by the first element
    -initialize resulting array
    -loop through those values
        -if resulting array is empty or current intervals first ele is greater than last intervals second, add the interval
        -elif current second element is greater than previous second element replace previous          second element
    -return the difference of each element in results array + 1
            {
            'a': [0, 8],
            'b': [1, 5],
            'c': [4, 7],
            'd': [9, 14],
            'e': [10, 15],
            'f': [11, 11],
            'g': [13, 13],
            'h': [16, 19],
            'i': [17, 22],
            'j': [18, 23],
            'k': [20, 20],
            'l': [21, 21]
        }
        'ababcbaca' 'defegde' 'hijhklij'
        
    
"""
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        letter_idx_mapping = collections.defaultdict(list)
        merged_intervals = []
        for i, letter in enumerate(S):
            if letter not in letter_idx_mapping:
                letter_idx_mapping[letter] = [i, i]
            else:
                letter_idx_mapping[letter][1] = i
        intervals = sorted(letter_idx_mapping.values())
        for interval in intervals:
            if not merged_intervals or interval[0] > merged_intervals[-1][1]:
                merged_intervals.append(interval)
            elif interval[1] > merged_intervals[-1][1]:
                merged_intervals[-1][1] = interval[1]
        return [x[1] - x[0] +1 for x in merged_intervals]