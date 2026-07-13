class Combo:
    def __init__(self, items: List[int]):
        self.items = items

    def __hash__(self):
        return hash(str(self.items))

    def __eq__(self, other):
        return self.items == other.items

    def with_new_item(self, item, freq=1):
        items_copy = list(self.items)
        for i in range(freq):
            items_copy.append(item)

        return Combo(items_copy)

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return str(self)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []

        def form_sum(i, target_left, combo):
            #print("i", i, "target", target_left, "combo", combo)

            if target_left == 0:
                combos.append(combo.items)
                return
            elif target_left < 0:
                return
            elif i >= len(candidates):
                return

            max_freq = target_left // candidates[i]
            #print("max freq", max_freq)

            for poss_freq in range(0, max_freq + 1):
                next_targ_left = target_left - (poss_freq * candidates[i])
                #print("calling recursively", next_targ_left)
                form_sum(i + 1, next_targ_left, combo.with_new_item(candidates[i], poss_freq))

        form_sum(0, target, Combo([]))

        return combos