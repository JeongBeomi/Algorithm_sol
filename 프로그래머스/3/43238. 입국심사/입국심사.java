class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        long start = 1, end = 1000000000L * n;
        
        while (start < end) {
            long mid = (start + end) / 2;
            long count = 0;
            
            for (int time : times) {
                count += mid / time;
                if (count >= n) break;
            }
            
            if (count >= n) {
                end = mid;
                answer = mid;
            } else {
                start = mid + 1;
            }
            
        }
        
        return answer;
    }
}