import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public void bfs(int s, int[][] computers, boolean[] visited) {
        int n = visited.length;
        Deque<Integer> dq = new ArrayDeque<Integer>();
        dq.offer(s);
        visited[s] = true;
        
        while (!dq.isEmpty()) {
            int idx = dq.poll();
            for (int ns = 0 ; ns < n; ns++) {
                if (!visited[ns] && computers[idx][ns] == 1) {
                    visited[ns] = true;
                    dq.offer(ns);
                }
            }
        }
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                answer++;
                bfs(i, computers, visited);
            }
        }
        
        
        return answer;
    }
}