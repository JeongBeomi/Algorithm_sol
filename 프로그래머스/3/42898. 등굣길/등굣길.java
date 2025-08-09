class Solution {
    static int[] dr = {-1, 0};
    static int[] dc = {0, -1};
    
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int[][] dp = new int[n][m];
        boolean[][] puddlesPos = new boolean[n][m];
        dp[0][0] = 1;
        
        for (int[] p : puddles) {
            puddlesPos[p[1] - 1][p[0] - 1] = true;
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (puddlesPos[i][j]) {
                    dp[i][j] = 0;
                    continue;
                }
                
                for (int d = 0; d < 2; d++) {
                    if (0 <= i + dr[d] && 0 <= j + dc[d]) {
                        dp[i][j] += dp[i + dr[d]][j + dc[d]];
                    }
                }
                dp[i][j] %= 1000000007;
            }
        }
        
        answer = dp[n - 1][m - 1];
        
        return answer;
    }
}