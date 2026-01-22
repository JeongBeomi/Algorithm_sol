import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        Deque<int[]> dq = new ArrayDeque<int[]>();
        // {현재 합산 숫자, 지금까지 연산을 진행한 숫자 인덱스}
        dq.offerLast(new int[]{0, 0});
        while(!dq.isEmpty()) {
            int[] sumArray = dq.pollFirst();
            
            // 모든 numbers를 사용하여 연산이 끝나면 해당 수가 타겟 넘버인지 확인
            if(sumArray[1] >= numbers.length) {
                if(sumArray[0] == target) answer++;
                continue;
            }
            
            // 다음 연산 대상 숫자를 더하거나 빼서 큐애 삽입
            dq.offerLast(new int[]{sumArray[0] + numbers[sumArray[1]], sumArray[1] + 1});
            dq.offerLast(new int[]{sumArray[0] - numbers[sumArray[1]], sumArray[1] + 1});
        }
        
        return answer;
    }
}