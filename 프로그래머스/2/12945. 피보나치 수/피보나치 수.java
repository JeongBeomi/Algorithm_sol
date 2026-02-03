class Solution {
    public int fibonacci(int idx, int[] dp) {
        if (idx > 0 && dp[idx] == 0) dp[idx] = (fibonacci(idx - 1, dp) + fibonacci(idx - 2, dp)) % 1234567;
        return dp[idx];
    }
    
    public int solution(int n) {
        int answer = 0;
        
        int[] dp = new int[n + 1];
        dp[1] = 1;
        answer = fibonacci(n, dp);
        
        return answer;
    }
}