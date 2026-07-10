class Solution {
    public boolean canJump(int[] nums) {
        /*
        2,3,1,1,4
        2 4

        3,2,1,0,4
        3 3 3 3
        Is current index <= a position we already found?
        if no, skip

        3,2,1,0,1,2
        3 3 3 3 

        */
        if (nums.length == 1) return true;

        int maxFound = -1;

        for (int i = 0; i < nums.length - 1; i++) {
            if (i == 0 || i <= maxFound) {
                int jumpPos = i + nums[i];
                // Cuz that's the maximum jump pos,
                // so if you can jump way more than the last element, then you can def jump to the last element
                if (jumpPos >= nums.length - 1) {
                    return true;
                }
                maxFound = Math.max(maxFound, jumpPos);
            }
        }
        return false;
    }
}