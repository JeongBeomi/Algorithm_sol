import java.util.Arrays;

class Solution {
    static int[][] numbers;
    static int[] dr = {0, 1, 0, -1};
    static int[] dc = {1, 0, -1, 0};
    
    public int rotation(int[] q) {
        int r = q[0] - 1, c = q[1] - 1;
        int minNum = numbers[r][c];
        int beforeNum = numbers[r][c];
        
        for (int d = 0; d < 4; d++) {
            while (q[0] - 1 <= r + dr[d] && r + dr[d] < q[2] && q[1] - 1 <= c + dc[d] && c + dc[d] < q[3]) {
                if (minNum > beforeNum) minNum = beforeNum;
                int tempNum = numbers[r + dr[d]][c + dc[d]];
                numbers[r + dr[d]][c + dc[d]] = beforeNum;
                beforeNum = tempNum;
                r += dr[d];
                c += dc[d];
            }
        }
        
        return minNum;
    }
    
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        numbers = new int[rows][columns];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                numbers[i][j] = i * columns + j + 1;
            }
        }
        
        for (int i = 0; i < queries.length; i++) {
            answer[i] = rotation(queries[i]);
        }
        
        return answer;
    }
}