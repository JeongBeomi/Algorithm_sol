import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int t = 0, returnTime = 0, cnt = 0, idx = 0;
        Arrays.sort(jobs, Comparator.comparingInt((int[] x)-> x[0]));
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] != b[1] ? a[1] - b[1] : a[0] - b[0]);
        
        // 작업 시작
        while (cnt < jobs.length) {
            while (idx < jobs.length && t >= jobs[idx][0]) {
                pq.add(jobs[idx]);
                idx++;
            }
            
            if (!pq.isEmpty()) {
                int[] jobDetail = pq.poll();
                t = Math.max(t, jobDetail[0]) + jobDetail[1];
                returnTime += t - jobDetail[0];
                cnt++;
            } else {
                t = jobs[idx][0];
            }
        }
        
        answer = returnTime / jobs.length;
        
        return answer;
    }
}