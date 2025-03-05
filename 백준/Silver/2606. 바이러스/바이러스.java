import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Queue;
import java.util.ArrayList;

public class Main {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    
    public static int bfs(int start) {
        int result = 0;
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(start);
        visited[start] = true;
        
        while (!q.isEmpty()) {
            int v = q.remove();
            for (int nv : graph[v]) {
                if (!visited[nv]) {
                    q.add(nv);
                    visited[nv] = true;
                    result++;
                }
            }
        }
        
        return result;
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        
        graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i ++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < m; i ++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }
        
        visited = new boolean[n + 1];
        System.out.println(bfs(1));
    }
}