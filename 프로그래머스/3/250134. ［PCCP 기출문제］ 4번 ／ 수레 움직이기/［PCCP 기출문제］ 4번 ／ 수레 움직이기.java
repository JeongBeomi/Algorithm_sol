class Solution {
    static int[] dr = {1, 0, -1, 0};
    static int[] dc = {0, 1, 0, -1};
    static int n, m;
    static int minCnt;
    static boolean arriveFlag = false;
    static boolean[][] redVisited;
    static boolean[][] blueVisited;
    static int redEndRow, redEndCol, blueEndRow, blueEndCol;

    public void dfs(int rr, int rc, int br, int bc, int dept) {
        // 가지치기
        if (dept > minCnt) {
            return;
        }

        // 레드 블루 둘다 도착 시
        if ((rr == redEndRow && rc == redEndCol) && (br == blueEndRow && bc == blueEndCol)) {
            arriveFlag = true;
            if (minCnt > dept) {
                minCnt = dept;
                return;
            }
        }

        // 이동
        for (int rd = 0; rd < 4; rd++) {
            for (int bd = 0; bd < 4; bd++) {
                // 빨간 수레 다음 좌표
                int nrr = rr + dr[rd], nrc = rc + dc[rd];
                if (rr == redEndRow && rc == redEndCol) {
                    nrr = rr;
                    nrc = rc;
                } else if (0 > nrr || nrr >= n || 0 > nrc || nrc >= m || redVisited[nrr][nrc]) {
                    break;
                } 

                // 파란 수레 다음 좌표
                int nbr = br + dr[bd], nbc = bc + dc[bd];
                if (br == blueEndRow && bc == blueEndCol) {
                    nbr = br;
                    nbc = bc;
                } else if (0 > nbr || nbr >= n || 0 > nbc || nbc >= m || blueVisited[nbr][nbc]) {
                    continue;
                }

                // 이동할 수 없는 상황 제거
                if ((nrr == nbr && nrc == nbc) || (nrr == br && nrc == bc && nbr == rr && nbc == rc)) { // 같은 좌표로 이동하려고 할 때 || 서로를 관통하려고 할때
                    continue;
                }

                // 이동
                redVisited[nrr][nrc] = true;
                blueVisited[nbr][nbc] = true;
                dfs(nrr, nrc, nbr, nbc, dept + 1);

                // 복귀 이미 목적지에 도착한 상태엿으면 방문처리 해둬야한다
                if (rr != redEndRow || rc != redEndCol) redVisited[nrr][nrc] = false;
                if (br != blueEndRow || bc != blueEndCol) blueVisited[nbr][nbc] = false;

            }
        }

    }

    public int solution(int[][] maze) {
        int answer = 0;
        n = maze.length;
        m = maze[0].length;
        minCnt = n * m + 1;
        redVisited = new boolean[n][m];
        blueVisited = new boolean[n][m];
        int redStartRow = 0, redStartCol = 0, blueStartRow = 0, blueStartCol = 0;

        // 시작 도착 좌표 찾기
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (maze[i][j] == 0) {
                    continue;
                } else if (maze[i][j] == 1) {
                    redStartRow = i;
                    redStartCol = j;
                } else if (maze[i][j] == 2) {
                    blueStartRow = i;
                    blueStartCol = j;
                } else if (maze[i][j] == 3) {
                    redEndRow = i;
                    redEndCol = j;
                } else if (maze[i][j] == 4) {
                    blueEndRow = i;
                    blueEndCol = j;
                } else if (maze[i][j] == 5) {
                    redVisited[i][j] = true;
                    blueVisited[i][j] = true;
                }
            }
        }

        redVisited[redStartRow][redStartCol] = true;
        blueVisited[blueStartRow][blueStartCol] = true;

        dfs(redStartRow, redStartCol, blueStartRow, blueStartCol, 0);
        
        if (arriveFlag) answer = minCnt;

        return answer;
    }
}