class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n]*n
        
        
        def fill(empty_matrix,n):
            value = 1
            r = 0
            c = 0
            dir = "left"
            while dir == "left":
                empty_matrix[r][c] = value
                value += 1
                c += 1
                if c == n:
                    dir = "down"
                    c -=1
                    r += 1
            while dir == "down":
                empty_matrix[r][c] = value
                value += 1
                r += 1
                if r == n:
                    dir = "right"
                    r -=1
                    c -= 1
            while dir == "right":
                empty_matrix[r][c] = value
                value += 1
                c -= 1
                if c < 0:
                    dir = "up"
                    c += 1
                    r-=1
            print(r,c)
            while dir == "up":
                empty_matrix[r][c] = value
                value += 1
                r -= 1
                if r < 0:
                    dir = "up"
                    c += 1
                    r-=1               
           
                
                
           
        fill(matrix,n)   
            
            
        
        
        return matrix
obj = Solution()
n=3
print(obj.generateMatrix(n))