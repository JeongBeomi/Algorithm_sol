import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int M;
    static int[][] dp = new int[31][31];
    
    public static int recur(int r, int c) {
        if (dp[r][c] == 0) {
            if (r == c || r == 0) {
                dp[r][c] = 1;
            } else {
                dp[r][c] = recur(r - 1, c - 1) + recur(r, c - 1); 
            }    
        }
        return dp[r][c];
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringTokenizer st;
        
        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            
            System.out.println(recur(N, M));
        }
        
    }
}