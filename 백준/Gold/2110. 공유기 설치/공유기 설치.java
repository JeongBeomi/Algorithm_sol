import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] answer = {0};
        
        int N = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        
        int[] pos = new int[N];
        for (int i = 0; i < N; i++) {
            pos[i] = Integer.parseInt(br.readLine());
        }
        
        Arrays.sort(pos);
        
        int lo = 1;
        int hi = pos[N - 1] - pos[0] + 1;
        
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            
            int cnt = 1;
            int idx = 0;
            for (int i = 1; i < N; i++) {
                if (pos[i] - pos[idx] >= mid){
                    idx = i;
                    cnt++;
                }
            }
            
            if (cnt >= C) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
            
        }
        
        System.out.println(lo - 1);
    }
}
