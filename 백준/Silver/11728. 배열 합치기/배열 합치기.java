import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.lang.StringBuilder;

public class Main {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] numbers1 = new int[n], numbers2 = new int[m];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            numbers1[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            numbers2[i] = Integer.parseInt(st.nextToken());
        }

        StringBuilder sb = new StringBuilder();
        int idx1 = 0, idx2 = 0;
        while(idx1 < n && idx2 < m) {
            if (numbers1[idx1] <= numbers2[idx2]) {
                sb.append(numbers1[idx1]).append(" ");
                idx1++;
            } else {
                sb.append(numbers2[idx2]).append(" ");
                idx2++;
            }
        }

        if (idx1 < n) {
            for (int i = idx1; i < n; i++) sb.append(numbers1[i]).append(" ");
        } else if (idx2 < m) {
            for (int i = idx2; i < m; i++) sb.append(numbers2[i]).append(" ");
        }

        System.out.println(sb.toString());
    }
}