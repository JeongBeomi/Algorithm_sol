import java.util.HashMap;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        int n = friends.length;
        HashMap<String, Integer> nameIdx = new HashMap<String, Integer>();
        int[] giftCnt = new int[n];
        
        // 각 이름마다 고유 인덱스 부여
        for (int i = 0; i < n; i++) {
            nameIdx.put(friends[i], i);
        }
        
        // 2차원 배열로 관리 giftHistory[준사람 인덱스][받은사람 인덱스]
        // 행렬을 한줄씩 추가한 이유는 선물 지수 계산을 위한 총 선물한 수와 총 받은 선물의 수 저장을 위함
        int[][] giftHistory = new int[n + 1][n + 1];
        for (String gift : gifts) {
            String[] history = gift.split(" ");
            giftHistory[nameIdx.get(history[0])][nameIdx.get(history[1])] += 1; // 선물한 수 추가
            giftHistory[nameIdx.get(history[0])][n] += 1;   // 총 선물한 수 추가
            giftHistory[n][nameIdx.get(history[1])] += 1;   // 총 받은 선물 수 추가
        }
        
        // 줄 선물 카운트
        for (int i = 0; i < n - 1; i++) {
            for (int j = i; j < n; j++) {
                int cnt1 = giftHistory[i][j];
                int cnt2 = giftHistory[j][i];
                if (cnt1 > cnt2) {
                    giftCnt[i] += 1;
                } else if (cnt1 < cnt2) {
                    giftCnt[j] += 1;
                } else {
                    // 서로 준 선물의 수가 같다면 선물 지수 비교
                    if (giftHistory[i][n] - giftHistory[n][i] > giftHistory[j][n] - giftHistory[n][j]) {
                        giftCnt[i] += 1;
                    } else if (giftHistory[i][n] - giftHistory[n][i] < giftHistory[j][n] - giftHistory[n][j]) {
                        giftCnt[j] += 1;
                    }
                }
            }
        }
        
        // 최대값 찾기
        for (int i = 0; i < n; i++) {
            if (answer < giftCnt[i]) answer = giftCnt[i];
        }
        
        return answer;
    }
}