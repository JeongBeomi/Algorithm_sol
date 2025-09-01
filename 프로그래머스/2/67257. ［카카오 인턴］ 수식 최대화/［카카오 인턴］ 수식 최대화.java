import java.util.Arrays;

class Solution {
    static String[] operator = {"+", "-", "*"};
    static String[] operatorPrecedence = new String[3];
    static boolean[] visited = new boolean[3];
    static long maxNum = 0;
    
    public void operatorPermutaion(int dept, String e) {
        if (dept >= 3) {
            System.out.println(Arrays.toString(operatorPrecedence));
            maxNum = Math.max(maxNum, Math.abs(recur(0, e)));
            return;
        }
        
        for (int i = 0; i < 3; i++) {
            if (!visited[i]) {
                visited[i] = true;
                operatorPrecedence[dept] = operator[i];
                operatorPermutaion(dept + 1, e);
                visited[i] = false;
            }
        }
        
    }
    
    public long recur(int dept, String e) {
        if (dept >= 3) {
            return Long.parseLong(e);
        }
        
        String[] expressionSplitList = e.split("\\" + operatorPrecedence[dept]);
        long sumNum = recur(dept + 1, expressionSplitList[0]);
        for (int i = 1; i < expressionSplitList.length; i++) {
            sumNum = calculate(sumNum, recur(dept + 1, expressionSplitList[i]), operatorPrecedence[dept]);
        }
        return sumNum;
        
    }
    
    public long calculate(long num1, long num2, String o) {
        long result = 0;
        if (o.equals("+")) {
            result = num1 + num2;
        } else if (o.equals("-")) {
            result = num1 - num2;
        } else if (o.equals("*")) {
            result = num1 * num2;
        }
        
        return result;
    }
    
    
    public long solution(String expression) {
        long answer = 0;
        
        operatorPermutaion(0, expression);
        answer = maxNum;
        
        return answer;
    }
}