class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String answer = "";
        
        int videoLen = Integer.parseInt(video_len.substring(0, 2) + video_len.substring(3, 5));
        int nowPos = Integer.parseInt(pos.substring(0, 2) + pos.substring(3, 5));
        int opStart = Integer.parseInt(op_start.substring(0, 2) + op_start.substring(3, 5));
        int opEnd = Integer.parseInt(op_end.substring(0, 2) + op_end.substring(3, 5));
        
        for (String command : commands) {
            // 오프닝 구간이면 무조건 오프닝 끝나는 시간으로
            if (opStart <= nowPos && nowPos <= opEnd) {
                nowPos = opEnd;
            }
            
            // 앞뒤 이동
            if (command.equals("prev")) {
                nowPos -= 10;
                if (nowPos % 100 > 59) nowPos -= 40;
                if (nowPos < 0) nowPos = 0;
            } else {
                nowPos += 10;
                if (nowPos % 100 > 59) nowPos += 40;
                if (nowPos > videoLen) nowPos = videoLen;
            }
            
            // 오프닝 구간이면 무조건 오프닝 끝나는 시간으로
            if (opStart <= nowPos && nowPos <= opEnd) {
                nowPos = opEnd;
            }
        }
        
       answer = String.format("%02d:%02d", nowPos / 100, nowPos % 100);
        
        
        return answer;
    }
}