
def lengthOfLongestSubstring(self, s: str) -> int:
    res = 0
    seen = {}
    left = 0

    # Sliding window approach
    for right, character in enumerate(s):
        if character in seen:
            left = max(left, seen[character] + 1)
        seen[character] = right
        res = max(res, right - left + 1)

    return res

# Time complexity is O(n)
# Space is O(1) because of the max size of the seen dictionary is 26