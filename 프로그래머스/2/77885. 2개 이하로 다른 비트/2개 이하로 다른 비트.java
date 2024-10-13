class Solution {
    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            answer[i] = f(numbers[i]);
        }
        return answer;
    }
    
    public long f(long x) {
        long result = x;
        long n = 0;
        while (x % 2  == 1) {
            n += 1;
            x /= 2;
        }
        if (n != 0) { n -= 1; }
        return result + (1L<<n);
    };
}