import java.util.ArrayList;

class Solution {
    static ArrayList<String> perList = new ArrayList<>();
    static boolean[] perVisited = new boolean[3];
    static String[] culs = {"+", "-", "*"}; 
    
    public void permutation(int dept, String culPer) {
        if (dept >= 3) {
            perList.add(culPer);
            return;
        }
        
        for (int i = 0; i < 3; i++) {
            if (!perVisited[i]) {
                perVisited[i] = true;
                permutation(dept + 1, culPer + culs[i]);
                perVisited[i] = false;
            } 
        }
        
    }
    
    public long recul(int dept, String e, String per) {
        if (dept >= 3) {
            return Long.parseLong(e);
        }
        
        String[] eSplitList = e.split("\\"+String.valueOf(per.charAt(dept)));
        long result = recul(dept + 1, eSplitList[0], per);
        
        for (int i = 1; i < eSplitList.length; i++) {
            result = calculater(per.charAt(dept), result, recul(dept + 1, eSplitList[i], per));
        }
        
        return result;
    }
    
    public long calculater(char c, long num1, long num2) {
        if (c == '+') {
            return num1 + num2;
        } else if (c == '-') {
            return num1 - num2;
        } else {
            return num1 * num2;
        }
    }
    
    public long solution(String expression) {
        long answer = 0;
        String culPer = "";
        
        permutation(0, culPer);
        
        for (String p : perList) {
            long total = Math.abs(recul(0, expression, p));
            if (answer < total) answer = total; 
        }
        
        return answer;
    }
}