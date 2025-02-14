import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;
import java.lang.StringBuilder;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Queue q = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            q.add(i + 1);
        }

        StringBuilder sb = new StringBuilder("<");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < k - 1; j++) {
                q.add(q.remove());
            }
            sb.append(q.remove());
            if (i != (n - 1)) {
                sb.append(", ");
            }
        }
        sb.append(">");
        System.out.println(sb);
    }
}