class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        
        l=1
        r=len(matrix)*len(matrix[0])
        
        
        while l<=r:
            mid=(l+r)//2
            
            row=math.ceil((mid/len(matrix[0])))-1
            
            if mid%len(matrix[0])-1==-1:
                c=len(matrix[0])-1
            else:
                c=mid%len(matrix[0])-1
            print(mid,row,c)
            if matrix[row][c]==target:
                return True 
            elif matrix[row][c]> target:
                r=mid-1
            else:
                l=mid+1
        return False
            



