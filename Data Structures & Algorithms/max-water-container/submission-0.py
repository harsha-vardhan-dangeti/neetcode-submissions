class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i, j = 0, len(heights)-1

        result = []

        max_volume = 0

        while(i < j):
            
            current_volume = (j-i) * min(heights[i],heights[j])

            if current_volume > max_volume:
                max_volume = current_volume

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1   
        
        return max_volume
        
            


        