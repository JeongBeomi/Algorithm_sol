class Solution {
    static boolean[][] chess;
    static int[] dr = {-1, -1, -1};
    static int[] dc = {0, -1, 1};
    static int cnt = 0;
    
    public void recur(int dept, int n) {
        // 배치가 끝나면 카운트 + 1
        if (dept >= n) {
            cnt++;
            return;
        }
        // dept행에 퀸을 놓을 열 정하기
        for (int i = 0; i < n; i++) {
            // 해당 행, 열에 퀸을 놓을수 있는지 확인하고 놓을 수 있다면 다음 행으로 이동
            boolean able = true;
            // 확인할 방향 선정 상, 좌상, 우상
            for (int d = 0; d < 3; d++) {
                // 해당 방향으로 이전에 배치한 행 만큼 반복 확인
                int r = dept, c = i;
                for (int j = 0; j < dept + 1; j++) {
                    int nr = r + dr[d], nc = c + dc[d];
                    if (0 <= nr && nr < n && 0 <= nc && nc < n && chess[nr][nc]) {
                        able = false;
                        break;
                    }
                    r = nr;
                    c = nc;
                }
                if (!able) break;
            }
            // 해당 위치에 놓을 수 있다면 퀸 배치후 다음 행 탐색을 위해 재귀 후 복귀
            if (able) {
                chess[dept][i] = true;
                recur(dept + 1, n);
                chess[dept][i] = false;
            }
        }
    }
    
    public int solution(int n) {
        int answer = 0;
        chess = new boolean[n][n];
        
        recur(0, n);
        answer = cnt;
        
        return answer;
    }
}