import java.util.*;

class Solution {
    static int[] dr = {1, 0, -1};
    static int[] dc = {0, 1, -1};
    
    public int[] solution(int n) {
        int[] answer = new int[n * (1 + n) / 2];
        
        int[][] triangle = new int[n][n];
        
        Deque<int[]> dq = new ArrayDeque<int[]>();
        dq.offer(new int[]{0, 0});
        triangle[0][0] = 1;
        int num = 2;
        int d = 0;
        
        while (!dq.isEmpty()) {
            int[] pos = dq.poll();
            int nr = pos[0] + dr[d], nc = pos[1] + dc[d];
            if (0 <= nr && nr < n && 0 <= nc && nc < n && triangle[nr][nc] == 0) {
                triangle[nr][nc] = num++;
                dq.offer(new int[]{nr, nc});
            } else {
                d = (d + 1) % 3;
                nr = pos[0] + dr[d];
                nc = pos[1] + dc[d];
                if (0 <= nr && nr < n && 0 <= nc && nc < n && triangle[nr][nc] == 0) {
                    triangle[nr][nc] = num++;
                    dq.offer(new int[]{nr, nc});
                }
            }
        }
        
        int idx = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i + 1; j++) {
                answer[idx] = triangle[i][j];
                idx++;
            }
        }
        
        return answer;
    }
}