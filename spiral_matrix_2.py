class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n]*n
        
        
        def fill(empty_matrix,n):
            row = 0
            col = 0
            val = 1
            if row == 0 and col == 0:
                for i in range(col,n):
                    empty_matrix[row][col] = val
                    val +=1
                    col +=1
            if row == 0 and col == n:
                col-= 1
                row +=1
                for i in range(row,n):
                    empty_matrix[row][col] = val
                    val +=1
                    row +=1
            if row == n and col == n-1:
                row -= 1
                col -=1
                for i in range(col):
                    empty_matrix[row][col] = val
                    val +=1
                    col -=1  
                 
            if row == n-1 and col ==0:
                row -=1
                for i in range(row):
                    empty_matrix[row][col] = val
                    val +=1
                    row -=1  
        fill(matrix,n)   
            
            
        
        
        return matrix
obj = Solution()
n=3
print(obj.generateMatrix(n))