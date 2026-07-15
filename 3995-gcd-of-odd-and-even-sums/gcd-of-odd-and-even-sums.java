class Solution {
    public int gcd(int a, int b) {
        while (b != 0) {
            int remainder = a % b;
            a = b;
            b = remainder;
        }
        return a;
    }

    public int gcdOfOddEvenSums(int n) {
        // 1 + 2 + 3 + 4 + ... = n(n+1)/2
        // 2 + 4 + 6 + 8 + ... = 2n(n+1)/2 = n(n+1)
        
        // 2 + 4 + 6 + 8 - 1 - 1 - 1 - 1
        // =1 + 3 + 5 + 7
        // n(n+1)-1*n
        // n(n+1)-n
        int sumEven = n * (n + 1);
        int sumOdd = sumEven - n;
        return gcd(sumOdd, sumEven);
    }
}