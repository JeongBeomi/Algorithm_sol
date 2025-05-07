import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] words = {"뻔", "데기"};
        int A = Integer.parseInt(br.readLine());
        int T = Integer.parseInt(br.readLine());
        int W = Integer.parseInt(br.readLine());
        int nowT = 0;
        int idx = -1;
        int repeatCnt = 2;

        while (nowT < T) {
            // 뻔 데기 x 2
            for (int i = 0; i < 2; i++) {
                if (++nowT == T) {
                    idx += W + 1;
                    break;
                } else {
                    idx += 2;
                }
            }
            if (nowT == T) break;

            // 뻔 x n , 데기 x n
            if (W == 0) {
                if(nowT + repeatCnt >= T) {
                    idx += T - nowT;
                    break;
                }
                nowT += repeatCnt;
                idx += 2 * repeatCnt;
            } else {
                idx += repeatCnt;
                if(nowT + repeatCnt >= T) {
                    idx += T - nowT;
                    break;
                }
                nowT += repeatCnt;
                idx += repeatCnt;
            }

            repeatCnt++;
        }

        System.out.println(idx % A);
    }
}