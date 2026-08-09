class Solution:
    def isPalindrome(self, s: str) -> bool:
        isalnum = lambda character: character.lower() in "abcdefghijklmnopqrstuvwxyz0123456789"
        
        i = 0
        j = len(s) - 1

        while i < j:
            if not isalnum(s[i]):
                i += 1
                continue
            if not isalnum(s[j]):
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True