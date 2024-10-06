class Solution {
    public String solution(String s) {
        String answer = "";
        String[] stringArray = s.split(" ");
        int maxNum, minNum;
        maxNum = minNum = Integer.parseInt(stringArray[0]);
        
        for (String num : stringArray) {
            int n = Integer.parseInt(num);
            if (maxNum < n) maxNum = n;
            if (minNum > n) minNum = n;
        }
        
        return minNum + " " + maxNum;
    }
}