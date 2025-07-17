import java.util.ArrayDeque;
import java.util.Deque;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    static int N;
    static int M;
    static int[][] container;
    static int[] dr = {0, 1, 0, -1};
    static int[] dc = {1, 0, -1, 0};
    
    public int crain (String[] storage, char c) {
        int cnt = 0;
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (container[i][j] == 0 && storage[i].charAt(j) == c) {
                    cnt++;
                    container[i][j] = 1;
                }
            }
        }
        
        return cnt;
    }
    
    public int lift (String[] storage, char c) {
        int cnt = 0;
        ArrayList<int[]> changePos = new ArrayList<int[]>();
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (container[i][j] == 0 && storage[i].charAt(j) == c) {
                    // bfs로 접근 가능한지 먼저 확인
                    boolean accessible = false;
                    ArrayList<int[]> temp = new ArrayList<int[]>();
                    Deque<int[]> dq = new ArrayDeque<int[]>();
                    boolean[][] visited = new boolean[N][M];
                    dq.offer(new int[]{i, j});
                    visited[i][j] = true;
                    temp.add(new int[]{i, j});
                    
                    while(!dq.isEmpty()) {
                        int[] pos = dq.poll();
                        for (int d = 0; d < 4; d++) {
                            int nr = pos[0] + dr[d], nc = pos[1] + dc[d];
                            if (0 > nr || N <= nr || 0 > nc || M <= nc || container[nr][nc] == 2) {
                                dq.clear();
                                accessible = true;
                                break;
                            } else {
                                if (!visited[nr][nc] && container[nr][nc] == 1) {
                                    dq.offer(new int[]{nr, nc});
                                    visited[nr][nc] = true;
                                    temp.add(new int[]{nr, nc});
                                }
                            }
                        }
                    } 
                    
                    // 접근 가능하면 꺼내기
                    if (accessible) {
                        cnt ++;
                        changePos.addAll(temp);
                    }
                }
            }
        }
        for (int[] p : changePos) {
            container[p[0]][p[1]] = 2;
        }
        
        return cnt;
    }
    
    public int solution(String[] storage, String[] requests) {
        int answer = 0;
        N = storage.length;
        M = storage[0].length();
        container = new int[N][M];
        answer = N * M;
        
        for (String request : requests) {
            if (request.length() > 1) {
                answer -= crain(storage, request.charAt(0));
            } else {
                answer -= lift(storage, request.charAt(0));
            }
        }
        
        return answer;
    }
}