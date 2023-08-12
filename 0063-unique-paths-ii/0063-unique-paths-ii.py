class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp = {(m-1, n-1): 1}

        # def dfs(r, c):
        #     if r==m or c==n or obstacleGrid[r][c]:
        #         return 0
        #     if (r, c) in dp:
        #         return dp[(r, c)]
        #     dp[(r, c)] = dfs(r+1, c) + dfs(r, c+1)
        #     return dp[(r, c)]
        # return dfs(0, 0)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
       
        if obstacleGrid[m-1][n-1] == 1: 
            return 0
        else:
            dp = [0]*n
            dp[n-1] = 1

            for i in reversed(range(m)):
                for j in reversed(range(n)):
                    if obstacleGrid[i][j]:
                        dp[j] = 0
                    elif j+1 < n:
                        dp[j] = dp[j] + dp[j+1]

        return dp[0]