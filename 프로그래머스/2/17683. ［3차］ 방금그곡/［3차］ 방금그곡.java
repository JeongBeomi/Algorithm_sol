class Solution {
    
    public String flatReplace(String melody) {
        return melody.replace("C#", "c")
            .replace("D#", "d")
            .replace("F#", "f")
            .replace("G#", "g")
            .replace("B#", "b")
            .replace("A#", "a");
    }
    
    public String solution(String m, String[] musicinfos) {
        String answer = "(None)";
        int maxT = 0;
        m = flatReplace(m);
        
        for (String musicinfo : musicinfos) {
            String[] info = musicinfo.split(",");
            info[3] = flatReplace(info[3]);
            int t = (Integer.parseInt(info[1].substring(0, 2)) - Integer.parseInt(info[0].substring(0, 2))) * 60 + Integer.parseInt(info[1].substring(3, 5)) - Integer.parseInt(info[0].substring(3, 5));
            
            // 시작 멜로디가 같은 부분 찾기
            for (int i = 0; i < t - m.length() + 1; i++) {
                if (info[3].charAt(i % info[3].length()) == m.charAt(0)) {
                    // 다음 멜로디들이 같은지 확인
                    boolean flag = true;
                    for (int j = 1; j < m.length(); j++) {
                        if (info[3].charAt((i + j) % info[3].length()) != m.charAt(j)) {
                            flag = false;
                            break;
                        }
                    }
                    // 마지막 멜로디 다음 문자가 #이면 다른 음정
                    if (flag && maxT < t) {
                        answer = info[2];
                        maxT = t;
                        break;
                    }
                }
            }
        }
        
        return answer;
    }
}