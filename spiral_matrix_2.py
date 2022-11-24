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
                while col < n:
                    empty_matrix[row][col] = val
                    val +=1
                    col +=1
            
            if row == 0 and col == n-1:
                while row < n:
                    empty_matrix[row][col] = val
                    val +=1
                    row +=1
            
            if row == n-1 and col == n-1:
                while col >= n:
                    empty_matrix[row][col] = val
                    val +=1
                    col -=1  
                    
            if row == n-1 and col ==0:
                while row >= n:
                    empty_matrix[row][col] = val
                    val +=1
                    row -=1  
        
        fill(matrix,n)   
            
            
        
        
        return matrix
obj = Solution()
n=3
print(obj.generateMatrix(n))