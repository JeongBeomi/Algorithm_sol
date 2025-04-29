import java.util.Arrays;

class Solution {
    static int N;
    static int[] promotions = {10, 20, 30, 40};
    static int[] selectedPromotions;
    
    public void recur(int dept, int[][] users, int[] emoticons, int[] answer) {
        // 7개의 이모티콘에 대한 할인율 선택이 끝나면 결과 구하기
        if (dept >= N) {
            int plusCnt = 0;
            int totalMoney = 0;
            for (int[] user : users) {
                int money = 0;
                for (int idx = 0; idx < N; idx++) {
                    // 해당 이모티콘이 사용자의 기준 할인율 이상이면 구매
                    if (user[0] <= selectedPromotions[idx]) {
                        money += emoticons[idx] * (100 - selectedPromotions[idx]) / 100;
                    }
                    // 지금까지 구매 금액이 사용자 기준 금액 이상이면 구매 취소, 이모티콘 플러스 서비스 가입
                    if (user[1] <= money) {
                        money = 0;
                        plusCnt++;
                        break;
                    }
                }
                totalMoney += money;
            }

            
            // 결과 값 갱신
            if (answer[0] < plusCnt) {
                answer[0] = plusCnt;
                answer[1] = totalMoney;
            } else if (answer[0] == plusCnt && answer[1] < totalMoney) {
                answer[1] = totalMoney;
            }
            return;
        }
        
        for (int promotion : promotions) {
            selectedPromotions[dept] = promotion;
            recur(dept + 1, users, emoticons, answer);
        }
        
        
    }
    
    public int[] solution(int[][] users, int[] emoticons) {
        int[] answer = {0, 0};
        N = emoticons.length;
        selectedPromotions = new int[N]; 
        
        // 4^7 16384가지 경우의 수 완전 탐색 맞나?..
        recur(0, users, emoticons, answer);
        
        return answer;
    }
}