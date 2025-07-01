import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Arrays;

class Solution {
    static int[][] numbers;
    static int[] dr = {0, 1, 0, -1};
    static int[] dc = {1, 0, -1, 0};
    
    public int rotation(int sr, int sc, int er, int ec) {
        boolean[][] visited = new boolean[er + 1][ec + 1];
        int minNum = numbers[sr][sc];
        int beforeNum = numbers[sr][sc];
        Deque<int[]> dq = new ArrayDeque<int[]>();
        dq.offer(new int[]{sr, sc});
        
        for (int d = 0; d < 4; d++) {
            while (!dq.isEmpty()) {
                int[] pos = dq.poll();
                int nr = pos[0] + dr[d], nc = pos[1] + dc[d];
                if (sr <= nr && nr <= er && sc <= nc && nc <= ec && !visited[nr][nc]) {
                    int temp = numbers[nr][nc];
                    if (minNum > temp) minNum = temp;
                    numbers[nr][nc] = beforeNum;
                    beforeNum = temp;
                    visited[nr][nc] = true;
                    dq.offer(new int[]{nr, nc});
                } else {
                    dq.offer(pos);
                    break;
                }
            }
        }
        
        return minNum;
    }
    
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        
        // 1 ~ rows * columns 숫자로 채워진 배열 만들기
        numbers = new int[rows][columns];
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < columns; c++) {
                numbers[r][c] = r * columns + c + 1;
            }
        }
        
        // 회전 수행
        for (int i = 0; i < queries.length; i++) {
            answer[i] = rotation(queries[i][0] - 1, queries[i][1] - 1, queries[i][2] - 1, queries[i][3] - 1);
        }
        
        return answer;
    }
}