import java.lang.StringBuilder;
import java.util.Arrays;

class Solution {
    public String solution(String s) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        boolean flag = true;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == ' ') {
                sb.append(c);
                flag = true;
            } else {
                if (flag) {
                    sb.append(Character.toUpperCase(c));
                    flag = false;
                } else {
                    sb.append(Character.toLowerCase(c));
                }
            }
        }
        
        answer = sb.toString();
        return answer;
    }
}