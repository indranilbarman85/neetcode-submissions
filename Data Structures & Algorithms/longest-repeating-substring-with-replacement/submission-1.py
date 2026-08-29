class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        left = 0
        best = 0

        for right in range(len(s)):
            count[s[right]] += 1  # char enters window

            # window invalid: too many chars to replace
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1  # char leaves window
                left += 1

            best = max(best, right - left + 1)

        return best
        