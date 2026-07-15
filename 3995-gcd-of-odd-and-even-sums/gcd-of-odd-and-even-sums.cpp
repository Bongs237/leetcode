class Solution {
public:
    int gcdOfOddEvenSums(int n) {
        // 1 + 2 + 3 + 4 + ... = n(n+1)/2
        // 2 + 4 + 6 + 8 + ... = 2n(n+1)/2 = n(n+1)
        
        // 2 + 4 + 6 + 8 - 1 - 1 - 1 - 1
        // =1 + 3 + 5 + 7
        // n(n+1)-1*n
        // n(n+1)-n
        
        // n(n+1)=n^2+n

        // n(n+1)-n= n^2+n-n = n^2

        // The gcd is just n... smh
        // This legit is fewer code than "add two integers"

        //int sumEven = n * (n + 1);
        //int sumOdd = sumEven - n;
        return n;
    }
};