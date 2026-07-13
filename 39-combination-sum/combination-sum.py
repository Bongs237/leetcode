class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # It's all in the recursion
        combos = []

        def form_sum(i, target_left, combo):
            if target_left == 0:
                combos.append(combo)
                return
            elif target_left < 0:
                return
            elif i >= len(candidates):
                return

            max_freq = target_left // candidates[i]

            for poss_freq in range(0, max_freq + 1):
                next_targ_left = target_left - (poss_freq * candidates[i])
                form_sum(i + 1, next_targ_left, combo + [candidates[i]] * poss_freq)

        form_sum(0, target, [])

        return combos