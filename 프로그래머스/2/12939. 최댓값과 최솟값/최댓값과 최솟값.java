import java.lang.StringBuilder;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] nums = s.split(" ");
        int maxNum = Integer.parseInt(nums[0]);
        int minNum = Integer.parseInt(nums[0]);
        
        for (int i = 1; i < nums.length; i++) {
            int num = Integer.parseInt(nums[i]);
            if (maxNum < num) {
                maxNum = num;
            } else if (minNum > num) {
                minNum = num;
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append(minNum).append(" ").append(maxNum);
        
        answer = sb.toString();
        return answer;
    }
}