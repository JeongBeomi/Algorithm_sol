import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.lang.StringBuilder;

public class Main {
    static int N;
    static int M;
    static int[] nums;
    static boolean[] visited;

    public static void recur(int dept, StringBuilder result) {
        if (dept >= M) {
            result.deleteCharAt(2 * M - 1);
            System.out.println(result.toString());
            return;
        }

        for (int idx = 0; idx < N; idx++) {
            if (!visited[idx]) {
                result.append(nums[idx]).append(" ");
                visited[idx] = true;
                recur(dept + 1, result);
                visited[idx] = false;
                result.delete(dept * 2, dept * 2 + 2);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        nums = new int[N];
        visited = new boolean[N];
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < N; i++) nums[i] = i + 1;

        recur(0, result);
    }
}