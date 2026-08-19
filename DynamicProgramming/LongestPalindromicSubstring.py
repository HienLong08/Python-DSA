# Longest Palindromic Substring
# Given a string s, find and return the longest palindromic substring.
# A palindrome is a string that reads the same forward and backward.
# Example 1:
# Input:  s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
# Input:  s = "cbbd"
# Output: "bb"
# Constraints:
# 1 <= len(s) <= 1000
# s consists only of digits and English letters.

with open("LongestPalindromicSubstring.INP", "r") as fin:
    data = fin.readlines()
    s = data[0].strip()

N = len(s)
Ds = [[False] * N for _ in range(N)]

for i in range(N):
    Ds[i][i] = True

Max = 1
Start = 0

for Length in range(2, N + 1):
    for i in range(N - Length + 1):
        j = i + Length - 1

        if s[i] == s[j] and (Length <= 2 or Ds[i + 1][j - 1]):
            Ds[i][j] = True

            if Length > Max:
                Max = Length
                Start = i

Result = s[Start:Start + Max]

with open("LongestPalindromicSubstring.OUT", "w") as fout:
    fout.write(Result)
print(Result)