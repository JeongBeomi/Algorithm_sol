class Solution {
    static int idx = 0; 
    public void hanoi(int[][] answer, int s, int e, int n) {
        if (n == 1) {
            answer[idx] = new int[] {s, e};
            idx++;
            return;
        }
        
        hanoi(answer, s, 6 - s - e, n - 1);
        answer[idx] = new int[] {s, e};
        idx++;
        hanoi(answer, 6 - s - e, e, n - 1);
        
    }
    
    public int[][] solution(int n) {
        // 정답 배열 길이 계산 (총 이동 횟수는 n - 1 크기의 탑을 두번이동시키고 n번 원판을 한번 이동시킴)
        int answerSize = 1;
        for (int i = 1; i < n; i++) {
            answerSize = answerSize * 2 + 1;
        }
        int[][] answer = new int[answerSize][2];
        
        /*
        높이가 n인 하노이 탑을 1번에서 3번으로 이동시키는 법
        1) n - 1 크기의 탑을 2번으로 이동
        2) n번 원판을 3번으로 이동
        3) n - 1 크기의 탑을 2번에서 3번으로 이동
        */
        hanoi(answer, 1, 3, n);
        
        return answer;
    }
}