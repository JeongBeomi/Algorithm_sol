import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.Deque;
import java.util.ArrayDeque;

public class Main {
    static int N;
    static int M;
    static int[][] miro;
    static int[] dr = {0, 1, 0, -1};
    static int[] dc = {1, 0, -1, 0};
    
    public static int bfs(int sr, int sc) {
        Deque<int[]> dq = new ArrayDeque<int[]>();
        dq.offer(new int[]{sr, sc, 1});
        miro[sr][sc] = 0;
        
        while (!dq.isEmpty()) {
            int[] pos = dq.poll();
            for (int d = 0; d < 4; d++) {
                int nr = pos[0] + dr[d], nc = pos[1] + dc[d];
                if (nr == N - 1 && nc == M - 1) return pos[2] + 1;
                if (0 <= nr && nr < N && 0 <= nc && nc < M && miro[nr][nc] == 1) {
                    miro[nr][nc] = 0;
                    dq.offer(new int[]{nr, nc, pos[2] + 1});
                }
            }
        }
        
        return -1;
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        miro = new int[N][M];
        
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                if (line.charAt(j) == '1') miro[i][j] = 1;
            }
        }
        
        System.out.println(bfs(0, 0));
        
    }
}