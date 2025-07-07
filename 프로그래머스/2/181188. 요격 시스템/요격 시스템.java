import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        Arrays.sort(targets, Comparator.comparing((int[] x) -> x[1]));
        int c = 0;
        for (int[] target : targets) {
            if (c > target[0]) continue;
            c = target[1];
            answer++;
        }
        
        return answer;
    }
}