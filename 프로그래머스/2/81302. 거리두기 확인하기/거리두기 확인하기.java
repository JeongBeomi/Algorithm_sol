import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
        
    public boolean bfs(String[] place, int sr, int sc) {
        boolean[][] visited = new boolean[5][5];
        Deque<int[]> dq = new ArrayDeque<int[]>();
        visited[sr][sc] = true;
        dq.add(new int[]{sr, sc, 0});
        
        while (!dq.isEmpty()) {
            int[] pos = dq.pollFirst();
            int r = pos[0], c = pos[1], l = pos[2];
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d], nc = c + dc[d], nl = l + 1;
                if (0 <= nr && nr < 5 && 0 <= nc && nc < 5 && !visited[nr][nc] && place[nr].charAt(nc) != 'X') {
                    visited[nr][nc] = true;
                    if (place[nr].charAt(nc) == 'P') return true;
                    if (nl < 2) dq.add(new int[]{nr, nc, nl});
                }
            }
        }
        
        return false;
    }
    
    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        
        for (int placeNum = 0; placeNum < 5; placeNum++) {
            boolean checkPlace = true;
            for (int i = 0; i < 5; i++) {
                if (!checkPlace) break;
                for (int j = 0; j < 5; j++) {
                    if (places[placeNum][i].charAt(j) == 'P' && bfs(places[placeNum], i, j)) {
                        checkPlace = false;
                        break;
                    }
                }
            }
            
            
            if (checkPlace) answer[placeNum] = 1;
        }
        
        return answer;
    }
}