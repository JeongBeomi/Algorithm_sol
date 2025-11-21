import java.util.ArrayDeque;
import java.util.Deque;


class Solution {
    boolean solution(String s) {
        boolean answer = true;

        Deque<Character> dq = new ArrayDeque<>();
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                dq.offer('(');
                continue;
            }
            
            // 닫히는 괄호 일 때
            if (dq.isEmpty()) {
                answer = false;
                break;
            }
            dq.pollLast();
        }
        
        if(!dq.isEmpty()) answer = false;

        return answer;
    }
}