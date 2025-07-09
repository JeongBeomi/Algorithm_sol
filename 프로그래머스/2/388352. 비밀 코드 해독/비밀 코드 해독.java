import java.util.HashSet;

class Solution {
    static int[] code;
    static int cnt;
    static int[][] Q;
    static int[] ANS;
    
    public boolean checkCode() {
        boolean result = true;
        
        for (int i = 0; i < Q.length; i++) {
            HashSet<Integer> codeSet = new HashSet<Integer>();
            for (int c : code) {
                codeSet.add(c);
            }
            
            int containsCnt = 0;
            for (int j = 0; j < 5; j++) {
                if (codeSet.contains(Q[i][j])) containsCnt++;
            }
            
            if (containsCnt != ANS[i]) {
                result = false;
                break;
            }
            
        }
        
        return result;
    }
    
    public void comb(int sn, int en, int dept) {
        if (dept >= 5) {
            if (checkCode()) {
                cnt++;
            }
            return;
        }
        
        for (int n = sn; n <= en - 4 + dept; n++) {
            code[dept] = n;
            comb(n + 1, en, dept + 1);
        }
    }

    public int solution(int n, int[][] q, int[] ans) {
        int answer = 0;
        code = new int[5];
        Q = q;
        ANS = ans;
        
        comb(1, n, 0);
        answer = cnt;
        
        return answer;
    }
}