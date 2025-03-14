import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int startMoney = Integer.parseInt(br.readLine());
        Investor BNP = new Investor("BNP", startMoney, 0);
        Investor TIMING = new Investor("TIMING", startMoney, 0);

        StringTokenizer st = new StringTokenizer(br.readLine());
        int stockTrend = 0;
        int beforeStockPrice = Integer.parseInt(st.nextToken());
        BNP.buyStock(beforeStockPrice);
        while (st.hasMoreTokens()) {
            int stockPrice = Integer.parseInt(st.nextToken());
            BNP.buyStock(stockPrice);

            if (stockPrice > beforeStockPrice) {
                if (stockTrend < 0) {
                    stockTrend = 1;
                } else {
                    stockTrend += 1;
                }
                if (stockTrend >= 3) TIMING.sellStock(stockPrice);
            } else if (stockPrice < beforeStockPrice) {
                if (stockTrend > 0) {
                    stockTrend = -1;
                } else {
                    stockTrend -= 1;
                }
                if (stockTrend <= -3) TIMING.buyStock(stockPrice);
            } else {
                stockTrend = 0;
            }

            beforeStockPrice = stockPrice;
        }

        String result = "SAMESAME";
        if (BNP.assets(beforeStockPrice) > TIMING.assets(beforeStockPrice)) {
            result = "BNP";
        } else if (BNP.assets(beforeStockPrice) < TIMING.assets(beforeStockPrice)) {
            result = "TIMING";
        }

        System.out.println(result);
    }

    static class Investor {
        String name;
        int money;
        int stock;

        Investor(String name, int money, int stock) {
            this.name = name;
            this.money = money;
            this.stock = stock;
        }

        public void buyStock(int stockPrice) {
            if (money >= stockPrice) {
                stock += money / stockPrice;
                money %= stockPrice;
            }
        }

        public void sellStock(int stockPrice) {
            if (stock > 0) {
                money += stock * stockPrice;
                stock = 0;
            }
        }

        public int assets(int stockPrice) {
            return money + stock * stockPrice;
        }
    }
}