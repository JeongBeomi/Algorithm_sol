import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
    static int R, C, W;
    static int[][] pascalTriangle;

    public static int pascalNum(int r, int c) {
        if (c == 0 || r == c) {
            pascalTriangle[r][c] = 1;
        } else if (pascalTriangle[r][c] == 0) {
            pascalTriangle[r][c] = pascalNum(r - 1, c - 1) + pascalNum(r - 1, c);
        }

        return pascalTriangle[r][c];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());
        pascalTriangle = new int[R + W - 1][C + W - 1];

        int sumNum = 0;
        for (int i = 0; i < W; i++) {
            for (int j = 0; j < i + 1; j++) {
                sumNum += pascalNum(R + i - 1, C + j - 1);
            }
        }

        System.out.println(sumNum);

    }
}