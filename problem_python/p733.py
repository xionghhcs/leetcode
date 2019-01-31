class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        ori_color = image[sr][sc]
        m, n  = len(image), len(image[0])

        def get_ans(r, c):
            image[r][c] = newColor
            if r -1 >=0 and image[r -1][c] == ori_color:
                get_ans(r - 1, c)

            if r + 1 < m and image[r +1][c] == ori_color:
                get_ans(r + 1, c)
            
            if c - 1 >= 0 and image[r][c - 1] == ori_color:
                get_ans(r, c - 1)
            
            if c + 1 < n and image[r][c + 1] == ori_color:
                get_ans(r, c + 1)
        
        if ori_color == newColor:
            return image
        
        if sr >=0 and sr < m and sc >=0 and sc < n:
            get_ans(sr, sc)
        return image
        