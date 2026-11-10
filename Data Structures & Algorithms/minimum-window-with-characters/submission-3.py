class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        l = 0
        missing = len(t)
        best_len = float('inf')
        best_start, best_end = 0, 0

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                if best_len > (right - l + 1):
                    best_len = min(best_len, right - l + 1)
                    best_end = right + 1
                    best_start = l
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1
        return s[best_start:best_end] if best_len != float('inf') else ''

