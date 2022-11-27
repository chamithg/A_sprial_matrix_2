class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for _ in range(n)]
        col_start = 0
        row_start = 0
        col_end = n
        row_end = n
        pos = 1
        
    
            
        while col_start <col_end or row_start< row_end:
            for i in range(col_start,col_end):
                matrix[row_start][i] = pos
                pos = pos+1
            row_start= row_start+ 1

            for i in range(row_start,row_end):
                matrix[i][col_end-1] = pos
                pos = pos+1
            col_end = col_end -1

            for i in reversed(range(col_start,col_end)):
                matrix[row_end-1][i] = pos
                pos = pos+1
            row_end = row_end -1

            for i in reversed(range(row_start,row_end)):
                matrix[i][col_start] = pos
                pos = pos+1
            col_start = col_start + 1

        return matrix
obj = Solution()
n=3
print(obj.generateMatrix(n))