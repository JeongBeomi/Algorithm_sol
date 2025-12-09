import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] numArray = new int[n];

        for (int i = 0; i < n; i++) {
            numArray[i] = Integer.parseInt(br.readLine());
        }

        int nowNum = 1;
        Deque<Integer> dq = new ArrayDeque<>();
        boolean able = true;
        ArrayList<String> answer = new ArrayList<String>();

        for (int idx = 0; idx < n; idx++) {
            // 수열을 만들 수 없을 경우
            if (nowNum > numArray[idx] && (dq.isEmpty() || dq.getLast() < numArray[idx])) {
                able = false;
                break;
            }

            if (nowNum <= numArray[idx]) {
                int count = numArray[idx] - nowNum + 1;
                for (int i = 0; i < count; i++) {
                    answer.add("+");
                    dq.add(nowNum);
                    nowNum++;
                }
                answer.add("-");
                dq.pollLast();
            } else {
                while (!dq.isEmpty() && dq.getLast() > numArray[idx]) {
                    dq.pollLast();
                    answer.add("-");
                }
                if (!dq.isEmpty() && dq.getLast() == numArray[idx]) {
                    dq.pollLast();
                    answer.add("-");
                } else {
                    able = false;
                    break;
                }
            }
        }

        if (able) {
            for (int j = 0; j < answer.size(); j++) {
                System.out.println(answer.get(j));
            }
        } else {
            System.out.println("NO");
        }
    }
}