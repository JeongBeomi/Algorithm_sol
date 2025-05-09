import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] cntArray;
        if (n < 5) {
            cntArray = new int[6];
        } else {
            cntArray = new int[n + 1];
        }
        cntArray[3] = 1;
        cntArray[5] = 1;

        for (int idx = 6; idx < n + 1; idx++) {
            if (cntArray[idx - 3] == 0 && cntArray[idx - 5] == 0) {
                cntArray[idx] = 0;
            } else if (cntArray[idx - 3] != 0 && cntArray[idx - 5] != 0) {
                cntArray[idx] = Math.min(cntArray[idx - 3], cntArray[idx - 5]) + 1;
            } else {
                cntArray[idx] = Math.max(cntArray[idx - 3], cntArray[idx - 5]) + 1;
            }
        }

        System.out.println(cntArray[n] == 0 ? -1 : cntArray[n]);

    }
}