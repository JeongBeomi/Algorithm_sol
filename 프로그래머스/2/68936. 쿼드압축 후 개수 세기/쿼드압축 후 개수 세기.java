class Solution {
    static int N;
    
    public void recur(int r, int c, int[][] arr, int[] answer) {
        int number = arr[r][c];
        boolean flag = false;
        
        for (int i = r; i < r + N; i++) {
            if (flag) break;
            for (int j = c; j < c + N; j++) {
                if (number != arr[i][j]) {
                    flag = true;
                    break;
                }
            }
        }
        
        if (!flag) {
            answer[number] += 1;
        } else {
            N /= 2;
            for (int i = r; i < r + N * 2; i += N) {
                for (int j = c; j < c + N * 2; j += N) {
                    recur(i, j, arr, answer);
                }
            }
            N *= 2;
        }
    }
    
    public int[] solution(int[][] arr) {
        int[] answer = {0, 0};
        N = arr.length;
        
        recur(0, 0, arr, answer);
        
        return answer;
    }
}