"""
Given an array S of length n and integer values,
we want to find the maximum contiguous subarray sum in S.
For example, if S = [1, -2, 3, 4, 5, -6],
the maximum subarray sum is 3+4+5=12.

sum(i) = max{ sum(i-1) + a[i], a[i] }
"""

#a = [1, -2, 3, 4, 5, -6]
a = [-2, -3, 4, -1, -2, 1, 5, -3]
s = [0] * len(a)
s[0] = a[0]

# fill array
for i in range(1, len(a)):
    if a[i] > s[i-1] + a[i]:
        s[i] = a[i]
    else:
        s[i] = s[i-1] + a[i]

print(max(s))

# find contiguous range
start, end = -1, s.index(max(s))
for i in range(end, -1, -1):
    if s[i] > 0:
        start = i
    else:
        break

print(start, end)
