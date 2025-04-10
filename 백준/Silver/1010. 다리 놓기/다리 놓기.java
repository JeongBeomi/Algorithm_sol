import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] bridgeCnt = new int[31][31];
    
    public static int comb (int n, int m) {
        if (bridgeCnt[n][m] != 0) {
            return bridgeCnt[n][m];
        }
        if (n == 0 || n == m) {
            bridgeCnt[n][m] = 1;
            return 1;
        }
        int cnt = comb(n, m - 1) + comb(n - 1, m - 1);
        bridgeCnt[n][m] = cnt;
        return cnt;
    }
    
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringTokenizer st;
        
        for (int i = 0; i < t; i ++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            
            System.out.println(comb(n, m));
        }
    }
}