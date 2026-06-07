class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        d={}
        dr={}
        db={}  
        flag =True
        for i in range(9):
            d[i]={}
            for j in range(9):
                box_i=(i//3)
                box_j=(j//3)
                box_num=box_i*3+box_j
                if j not in dr.keys():
                        dr[j]={}
                if box_num not in db.keys():
                    db[box_num]={}

                if board[i][j]!=".":
                    if board[i][j] in d[i].keys():
                        flag=False
                    else:
                        d[i][board[i][j]]=1
                    if board[i][j] in dr[j].keys():
                        flag=False
                    else:
                        dr[j][board[i][j]]=1
                    if board[i][j] in db[box_num].keys():
                        flag = False
                    else: 
                        db[box_num][board[i][j]]=1
        return flag
                       

                    
                    

        