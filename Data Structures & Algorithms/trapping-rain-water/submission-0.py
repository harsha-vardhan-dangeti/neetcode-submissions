class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_list = [0] 
        suffix_list = [0] * len(height)
        suffix_list[-1] = 0
        min_list = [0] * len(height)
        res = [0] * len(height)
        res_sum = 0

        m_l = 0
        m_r = 0 

        for i in range(1, len(height)):
            m_l = max(height[i-1],m_l)
            prefix_list.append(m_l)
        #print(prefix_list)
        for i in range(len(height)-2, -1, -1):
            m_r = max(height[i+1],m_r)
            suffix_list[i] = m_r
        #print(suffix_list)

        for i in range(len(height)):
            min_list[i] = min(prefix_list[i], suffix_list[i])
        #print(min_list)
        for i in range(len(height)):
            current = min_list[i] - height[i]
            res[i] = 0 if current < 0 else current
            res_sum += res[i]
        
        return res_sum
