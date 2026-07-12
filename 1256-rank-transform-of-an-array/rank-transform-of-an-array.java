class Solution {
    public int[] arrayRankTransform(int[] arr) {
        TreeMap<Integer, Integer> rank = new TreeMap<>();
        int[] ans = new int[arr.length];

        for (int num : arr) {
            rank.put(num, 0);
        }

        int currRank = 1;
        Integer prev = null;
        for (Map.Entry<Integer, Integer> entry : rank.entrySet()) {
            if (prev != null && entry.getKey() > prev) {
                currRank++;
            }
            rank.put(entry.getKey(), currRank);
            prev = entry.getKey();
        }

        for (int i = 0; i < arr.length; i++) {
            ans[i] = rank.get(arr[i]);
        }
        return ans;
    }
}