class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        int n = schedules.length;
        answer = n;
        
        for (int i = 0; i < n; i++) {
            int yoil = startday - 1;    // 0~6 = 월~일
            int schedule = schedules[i] + 10;
            if (schedule % 100 >= 60) {
                schedule += 40;
            }
            
            for (int j = 0; j < timelogs[i].length; j++) {
                if (yoil >= 5) {    // 토, 일 패스
                    yoil = (yoil + 1) % 7;
                    continue;
                }
                if (timelogs[i][j] > schedule) {   // 지각
                    answer--;
                    break;
                }
                yoil = (yoil + 1) % 7;
            }
        }
        
        return answer;
    }
}