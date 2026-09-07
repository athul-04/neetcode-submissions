class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=-2
        
        for i in range(0,len(matrix)):
            # print(matrix[i][0])
            if matrix[i][0]==target: return True
            elif matrix[i][0]>target:
                row=i-1
                break
        

        row= len(matrix)-1 if row==-2 else row
        if row==-1:return False

        low=0
        high=len(matrix[row])-1

        while low<=high:
            mid=int(low+(high-low)/2)

            if matrix[row][mid]==target:return True

            elif matrix[row][mid]<target:
                low=mid+1
            else:
                high=mid-1
            
        return False

