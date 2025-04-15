import java.util.Arrays;
import java.util.ArrayList;
import java.util.Deque;
import java.util.ArrayDeque;

class Solution {
    static int[][] storageMap;
    static int r;
    static int c;
    static int[] dr = {0, 1, -1, 0};
    static int[] dc = {1, 0, 0, -1};
    
    public int crain(String request, String[] storage) {
        int cnt = 0;
        
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (request.charAt(0) == storage[i].charAt(j) && storageMap[i][j] == 0) {
                    cnt++;
                    storageMap[i][j] = 1;
                }
            }
        }
        
        return cnt;
    }
    
    public int lift(String request, String[] storage) {
        int cnt = 0;
        ArrayList<int[]> changePos = new ArrayList<>();
        
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (request.charAt(0) == storage[i].charAt(j) && storageMap[i][j] == 0) {
                    if (bfs(i, j)) {
                        cnt++;
                        changePos.add(new int[]{i, j});
                    }
                }
            }
        }
        
        for (int[] pos : changePos) {
            int x = pos[0], y = pos[1];
            storageMap[x][y] = 1;
        }
        
        return cnt;
    }
    
    public boolean bfs(int i, int j) {
        boolean result = false;
        boolean[][] visited = new boolean[r][c];
        Deque<int[]> dq = new ArrayDeque<>();
        dq.offerLast(new int[]{i, j});
        visited[i][j] = true;
        
        while (!dq.isEmpty()) {
            int[] pos = dq.pollFirst();
            int x = pos[0], y = pos[1];
            for (int d = 0; d < 4; d++) {
                int nx = dr[d] + x, ny = dc[d] + y;
                if (0 <= nx && nx < r && 0 <= ny && ny < c) {
                    if (storageMap[nx][ny] != 0 && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        dq.offerLast(new int[]{nx, ny});
                    }
                } else {
                    result = true;
                    dq = new ArrayDeque<>();
                    break;
                }
            }
        }
        
        return result;
    }
    
    public int solution(String[] storage, String[] requests) {
        r = storage.length;
        c = storage[0].length();
        int answer = r * c;
        storageMap = new int[r][c];
        
        for (String request : requests) {
            if (request.length() == 1) {
                answer -= lift(request, storage);
            } else {
                answer -= crain(request, storage);
            }
        }
        
        return answer;
    }
}