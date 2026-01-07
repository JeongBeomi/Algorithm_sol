class Solution {
    public int solution(int n) {
        int answer = 1;
        int sumNum = 0;
        int minNum = 0;
        for (int i = 1; i < n; i++) {
            sumNum += i;
            while (sumNum > n) {
                sumNum -= minNum++;
            }
            if (sumNum == n) answer++;
        }
        
        return answer;
    }
}