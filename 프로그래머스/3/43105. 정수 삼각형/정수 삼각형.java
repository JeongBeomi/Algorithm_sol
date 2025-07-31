import java.util.Arrays;

class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int n = triangle.length;
        
        int[][] dp = new int[n][];
        for (int i = 0; i < n; i++) dp[i] = new int[i + 1];
        dp[0][0] = triangle[0][0];
        
        for (int r = 1; r < n; r++) {
            for (int c = 0; c < r + 1; c++) {
                if (c - 1 >= 0) dp[r][c] = Math.max(dp[r][c], dp[r - 1][c - 1] + triangle[r][c]);
                if (c < r) dp[r][c] = Math.max(dp[r][c], dp[r - 1][c] + triangle[r][c]);
            }
        }
        
        for (int j = 0; j < n; j++) answer = Math.max(answer, dp[n - 1][j]);
        
        return answer;
    }
}