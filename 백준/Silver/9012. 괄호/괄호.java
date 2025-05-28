import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;

        for (int i = 0; i < n; i++) {
            String result = "YES";
            String words = br.readLine();
            Deque<Character> dq = new ArrayDeque<>();

            for (int j = 0; j < words.length(); j++) {
                char c = words.charAt(j);
                if (c == '(') {
                    dq.offer('(');
                } else {
                    if (!dq.isEmpty()) {
                        dq.pollLast();
                    } else {
                        result = "NO";
                        break;
                    }
                }
            }

            if (!dq.isEmpty()) {
                result = "NO";
            }

            System.out.println(result);
        }

    }
}