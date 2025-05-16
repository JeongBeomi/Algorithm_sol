import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n + 1];
        dp[1] = 1;

        for (int i = 2; i <= n; i++) {
            int min = i;
            for (int j = 1; j <= (int) Math.sqrt(i); j++) {
                min = Math.min(min, 1 + dp[i - j * j]);
            }
            dp[i] = min;
        }

        System.out.println(dp[n]);
    }
}