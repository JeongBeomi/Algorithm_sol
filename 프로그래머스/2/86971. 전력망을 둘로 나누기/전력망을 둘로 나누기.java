import java.util.ArrayList;
import java.util.Deque;
import java.util.ArrayDeque;

class Solution {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    
    public int bfs(int start) {
        int result = 1;
        Deque<Integer> dq = new ArrayDeque<Integer>();
        dq.offerLast(start);
        visited[start] = true;
        
        while (!dq.isEmpty()) {
            int v = dq.pollFirst();
            for (int nv : graph[v]) {
                if (!visited[nv]) {
                    visited[nv] = true;
                    result++;
                    dq.offerLast(nv);
                }
            }
        }
        
        return result;
    }
        
    public int solution(int n, int[][] wires) {
        int answer = n;
        // 탐색용 그래프 만들기
        graph = new ArrayList[n + 1];
        for (int i = 0; i < n + 1; i++) {
            graph[i] = new ArrayList<Integer>();
        }
        
        for (int[] wire : wires) {
            graph[wire[0]].add(wire[1]);
            graph[wire[1]].add(wire[0]);
        }
        
        // 제외할 한가지 간선을 선택하고, 한개의 노드에 대해서만 탐색
        for (int[] wire : wires) {
            visited = new boolean[n + 1];
            visited[wire[0]] = true;    // 해당 간선을 제외 했기 때문에 방문처리하여 가지 못하도록 처리
            int cnt = bfs(wire[1]);
            
            // 두 그룹의 숭전탑 개수 차이가 적으면 answer 갱신
            int d = Math.abs(cnt - (n - cnt));
            if (answer > d) {
                answer = d;
            }
        }
        
        return answer;
    }
}