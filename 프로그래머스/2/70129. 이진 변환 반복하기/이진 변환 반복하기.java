class Solution {
    public int[] solution(String s) {
        int[] answer = {0, 0};
        
        while (!s.equals("1")) {
            int l = s.length();
            int num = s.replaceAll("0","").length();
            answer[0]++;
            answer[1] += l - num;
            
            s = Integer.toString(num, 2);
        }
        
        return answer;
    }
}