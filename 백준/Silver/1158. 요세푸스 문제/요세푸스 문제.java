import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.lang.StringBuilder;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        StringBuilder sb = new StringBuilder("<");
        
        ArrayList<Integer> nums = new ArrayList<Integer>();
        for (int i = 1; i <= n; i++) {
            nums.add(i);
        }
        
        int idx = 0;
        while (!nums.isEmpty()) {
            idx = (idx + k - 1) % nums.size();
            sb.append(nums.remove(idx));
            if (!nums.isEmpty()) sb.append(", ");
        }
        sb.append(">");
        
        System.out.println(sb.toString());
    }
}