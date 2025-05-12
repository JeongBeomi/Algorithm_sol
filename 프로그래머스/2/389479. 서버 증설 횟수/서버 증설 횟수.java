import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Arrays;

class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        Deque<int[]> dq = new ArrayDeque<>();
        int severCnt = 0;
        
        for (int i = 0; i < 24; i++) {
            // 이전 증설한 서버가 닫히는지 확인
            if (!dq.isEmpty()) {
                int[] severAddInfo = dq.element();
                if (i - severAddInfo[0] >= k) {
                    severCnt -= severAddInfo[1];
                    dq.poll();
                }
                
            }
            
            // 이용자 수에 맞게 서버 증설이 필요한지 확인
            // 필요한 서버개수
            int requestSeverCnt = players[i] / m;
            
            if (requestSeverCnt > severCnt) {
                int addSeverCnt = requestSeverCnt - severCnt;
                dq.offer(new int[]{i, addSeverCnt});
                severCnt += addSeverCnt;
                answer += addSeverCnt;
            }
        }
        
        
        return answer;
    }
}