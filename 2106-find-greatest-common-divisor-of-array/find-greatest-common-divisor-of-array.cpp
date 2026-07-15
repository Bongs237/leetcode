class Solution {
public:
    int findGCD(vector<int>& nums) {
        int small = 1001;
        int large = 0;

        for (int num : nums) {
            small = min(small, num);
            large = max(large, num);
        }

        // gcd(small, large)
        while (large != 0) {
            int rem = small % large;
            small = large;
            large = rem;
        }
        return small;
    }
};