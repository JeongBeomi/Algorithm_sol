class Solution {
    public int solution(int n, int w, int num) {
        int answer = 0;
        
        int commonHeight = n / w;     // 모든 열의 공통 높이 (1 ~)  
        int higherColCnt = n % w;           // 높이가 1씩 더 높아지는 열의 개수
        
        int row = (num - 1) / w + 1;        // 목표 박스가 현재 존재하는 높이 (1 ~)
        
        int col;    // 목표 박스가 적재되어 있는 열
        if (row % 2 == 1) { // 높이가 홀수 -> 왼쪽부터 박스 적재
            col = (num - 1) % w;    
        } else {    // 높이가 짝수 -> 오른쪽부터 박스 적재
            col = w - (num - 1) % w - 1;
        }
        
        answer = commonHeight - row + 1;
        
        // 높이가 1씩 더 높아지는 열일 경우 추가해주기
        if (higherColCnt > 0) {
            if (commonHeight % 2 == 0 && 0 <= col && col < higherColCnt) {
                answer++;
            } else if (commonHeight % 2 == 1 && w - higherColCnt <= col && col < w) {
                answer++;
            }
        }
        
        return answer;
    }
}