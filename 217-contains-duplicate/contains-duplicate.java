class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> stuff = new HashSet<>();
        for (int num : nums) {
            if (stuff.contains(num)) {
                return true;
            }
            stuff.add(num);
        }

        return false;
    }
}