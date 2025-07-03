import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long s = Long.parseLong(br.readLine());
        long sumNum = 0;
        long cnt = 0;
        for (long i = 1; i <= s; i++) {
            sumNum += i;
            cnt++;
            if (sumNum >= s) break;
        }
        if (sumNum > s) cnt--;
        System.out.println(cnt);
    }
}