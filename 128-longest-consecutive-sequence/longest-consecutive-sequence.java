class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length <= 1) return nums.length;

        HashSet<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        int ans = 1;

        for (int num : nums) {
            if (numSet.contains(num - 1)) {
                continue;
            }

            int curr = num;
            int seq = 0;
            while (numSet.contains(curr)) {
                seq++;
                curr++;
                ans = Math.max(ans, seq);
            }

            if (ans > nums.length / 2) {
                break;
            }
        }
        return ans;
    }
}