class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        rain_water = 0
        left_wall, right_wall = 0, len(height) - 1
        start, end = 1, len(height)-2
        while start <= end:
            # Calculating rain water on the left side
            if height[left_wall] <= height[right_wall]:
                # Start is greater than left wall, no rain water can be trapped
                if height[start] > height[left_wall]:
                    left_wall = start
                # Rain water is trapped
                else:
                    rain_water += (height[left_wall] - height[start])
                start += 1
            # Calculating rain water on the right side
            else:
                # End is greater than Right wall, no rain water can be trapped
                if height[end] > height[right_wall]:
                    right_wall = end
                # Rain water is trapped
                else:
                    rain_water += (height[right_wall] - height[end])
                end -= 1
        return rain_water