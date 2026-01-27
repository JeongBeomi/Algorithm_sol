import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;

class Solution {    
    public void permutation(Set<Integer> numSet, String[] numberArray, boolean[] visited, int target, int dept, StringBuilder sb) {
        if (target == dept) {
            numSet.add(Integer.parseInt(sb.toString()));
            return;
        }
        
        for (int idx = 0; idx < numberArray.length; idx++) {
            if (!visited[idx]) {
                sb.append(numberArray[idx]);
                visited[idx] = true;
                permutation(numSet, numberArray, visited, target, dept + 1, sb);
                sb.deleteCharAt(dept);
                visited[idx] = false;
            }
        }
    }
    
    public int solution(String numbers) {
        int answer = 0;
        
        Set<Integer> numSet = new HashSet<Integer>();   // 중복 숫자 제외를 위해 Set 자료형 사용
        StringBuilder sb;
        boolean[] visited;
        // numbers에서 i 개를 뽑았을 때 만들수 있는 숫자 순열 만들기
        for (int i = 1; i <= numbers.length(); i++) {
            sb = new StringBuilder();
            visited = new boolean[numbers.length()];
            permutation(numSet, numbers.split(""), visited, i, 0, sb);
        }
        
        // 만든 숫자 순열을 순회하며 소수가 몇개 인지 확인
        System.out.println(numSet);
        for (int num : numSet) {
            if (num < 2) continue;
            answer++;
            for (int n = 2; n * n <= num; n++) {
                if (num % n == 0) {
                    answer--;
                    break;
                }
            }
        }
        
        return answer;
    }
}