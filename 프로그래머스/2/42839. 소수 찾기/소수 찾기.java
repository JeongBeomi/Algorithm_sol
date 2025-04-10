import java.util.Set;
import java.util.HashSet;
import java.lang.StringBuilder;

class Solution {
    static String[] numberArray;
    static Set<Integer> numberSet = new HashSet<>();
    static boolean[] visited;
    
    public void permutations(int target, int nowIdx, StringBuilder num) {
        if (target <= nowIdx) {
            int number = Integer.parseInt(num.toString());
            if (number > 1) numberSet.add(number);
        } else {
            for (int i = 0; i < numberArray.length; i++) {
                if (!visited[i]) {
                    visited[i] = true;
                    num.append(numberArray[i]);
                    permutations(target, nowIdx + 1, num);
                    num.deleteCharAt(nowIdx);
                    visited[i] = false;
                }
            }
        }
        
    }
    
    public int solution(String numbers) {
        int answer = 0;
        numberArray = numbers.split("");
        StringBuilder sb;
        for (int i = 1; i < numberArray.length + 1; i++) {
            visited = new boolean[numberArray.length];
            sb = new StringBuilder();
            permutations(i, 0, sb);    
        }
        
        for (int number : numberSet) {
            answer++;
            for (int i = 2; i * i <= number; i++) {
                if (number % i == 0) {
                    answer--;
                    break;
                }
            }
        }
        
        return answer;
    }
}