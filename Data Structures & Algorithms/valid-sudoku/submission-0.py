class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # for row
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[i][j]==".":continue
                if board[i][j] in seen:
                    print("In First") 
                    print(i,j)
                    return False
                seen.add(board[i][j])
            seen.clear()
        
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[j][i]==".":continue
                if board[j][i] in seen: 
                    print("In second") 
                    print(j,i)
                    return False
                seen.add(board[j][i])
            seen.clear()
        
        for i in range(0,9,3):
            seen=set()
            for j in range(0,9,3):
                row=i
                col=j

                while(row<i+3 and col<j+3):
                    if board[row][col]==".":
                        col+=1
                        if col>=j+3:
                            col=j
                            row+=1
                        continue
                    if board[row][col] in seen: 
                        print("In Third")
                        print(row,col,board[row][col])
                        print(seen)
                        return False
                    seen.add(board[row][col])
                    col+=1
                    if col>=j+3:
                        col=j
                        row+=1
                seen.clear()
        return True
        
                

                    


        
        
        