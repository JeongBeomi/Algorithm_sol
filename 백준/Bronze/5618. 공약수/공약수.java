import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        InputStreamReader reader = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(reader);

        int n = Integer.parseInt(in.readLine());
        StringTokenizer st = new StringTokenizer(in.readLine());

        int gcd = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n - 1; i++) {
            gcd = GCD(gcd, Integer.parseInt(st.nextToken()));
        }

        int sqrtGcd = (int) Math.sqrt(gcd);
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 1; i <= sqrtGcd; i++) {
            if (gcd % i == 0){
                answer.add(i);
                if (gcd / i != i) {
                    answer.add(gcd / i);
                }
            }
        }
        Collections.sort(answer);
        for (int i = 0; i < answer.size(); i++) {
            System.out.println(answer.get(i));
        }

    }

    public static int GCD(int a, int b) {
        if (a % b == 0) {
            return b;
        } else {
            return GCD(b, a % b);
        }
    }
}