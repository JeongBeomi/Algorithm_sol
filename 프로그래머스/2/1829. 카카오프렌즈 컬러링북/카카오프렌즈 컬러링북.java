import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    static int[] dr = {0, 1, 0, -1};
    static int[] dc = {1, 0, -1, 0};
    
    public int bfs(int sr, int sc, int[][] picture, boolean[][] visited) {
        int cnt = 1;
        int N = picture.length, M = picture[0].length;
        Deque<int[]> dq = new ArrayDeque<int[]>();
        dq.offer(new int[]{sr, sc});
        visited[sr][sc] = true;
        int target = picture[sr][sc];
        
        while(!dq.isEmpty()) {
            int[] pos = dq.poll();
            for (int d = 0; d < 4; d++) {
                int nr = pos[0] + dr[d], nc = pos[1] + dc[d];
                if (0 <= nr && nr < N && 0 <= nc && nc < M && !visited[nr][nc] && picture[nr][nc] == target) {
                    cnt++;
                    visited[nr][nc] = true;
                    dq.offer(new int[]{nr, nc});
                }
            }
        }
        
        
        return cnt;
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        boolean[][] visited = new boolean[m][n];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] != 0 && !visited[i][j]) {
                    int cnt = bfs(i, j, picture, visited);
                    numberOfArea++;
                    if (maxSizeOfOneArea < cnt) maxSizeOfOneArea = cnt;
                }
            }
        }
        
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}