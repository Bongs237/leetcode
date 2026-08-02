class Solution:
    def minimumPushes(self, word: str) -> int:
        # If theres 8 distinct letters in word, you can remap so every keypad has one letter (8 presses)
        # If 9, 8 presses + two presses on one 8+2*1 = 10
        # if 10, 8+2*2
        
        # if 17-24, third press
        # if 25, 26 - fourth press on 7 and 9
        max_press = math.ceil(len(word) / 8)

        ans = 0

        if max_press >= 1:
            ans += min(len(word), 8)
        if max_press >= 2:
            ans += min((len(word) - 8) * 2, 8 * 2)
        if max_press >= 3:
            ans += min((len(word) - 8 * 2) * 3, 8 * 3)
        if max_press >= 4:
            if len(word) == 25:
                ans += 4
            else: # 26
                ans += 8

        return ans