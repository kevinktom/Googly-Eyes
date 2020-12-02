class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        """
        PseudoCode:
            -sort by first element reversed, then second element ascending
                -sort by the first element because you want to work with the taller people first since shorter people don't matter for their relative position
            [7,0], [7,1], [6,1], [5,0], [5,2], [4,4]
            -empty answer array
            -loop through the above sorted array
            -if the answer array is empty, append the element
                -for the first element
            -insert people at index of second element
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        answer = []
        for person in people:
            answer.insert(person[1], person)
        return answer