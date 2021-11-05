

class Solution:
    def solveNQueens(self, n: int):
        if not n: return []
        board = [['.'] * n for _ in range(n)]
        res = []
        def isVaild(board,row, col):
            #判断同一列是否冲突
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False
            # 判断左上角是否冲突
            i = row -1
            j = col -1
            while i>=0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # 判断右上角是否冲突
            i = row - 1
            j = col + 1
            while i>=0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def backtracking(board, row, n):
            # 如果走到最后一行，说明已经找到一个解
            if row == n:
                temp_res = []
                for temp in board:
                    temp_str = "".join(temp)
                    temp_res.append(temp_str)
                res.append(temp_res)
            for col in range(n):
                if not isVaild(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtracking(board, row+1, n)
                board[row][col] = '.'
        backtracking(board, 0, n)
        return res

cc = Solution()
aa = cc.solveNQueens(4)
print(aa)


class Solution {
public:
    /**
     * 
     * @param n int整型 the n
     * @return int整型
     */
    //diagonal1代表"/"，diagonal2代表“\”
    int dfs(int c, int diagonal1, int diagonal2, int r, int n){
        int ans = 0;
        if(r >= n){
            return 1;
        }
        //枚举第r行的第i列
        for(int i = 1; i <= n; ++i){
            if(!(c & (1<<(i-1))) && !(diagonal1 & (1<<(i+r))) && !(diagonal2 & (1<<(n-i+r+1)))){
                ans+=dfs(c | (1<<(i-1)), diagonal1 | (1<<(i+r)), diagonal2 | (1<<(n-i+r+1)), r+1, n);
            }
        }
        return ans;
    }
    int Nqueen(int n) {
        // write code here
        return dfs(0, 0, 0, 0, n);
    }
};
