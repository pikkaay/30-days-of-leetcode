'''Longest Palindromic Substring

Solution
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''





def longestPalindrome(s):
    if len(s) == 0:
        return ''
    start = 0
    end = 0
    i = 0
    while i < len(s):
        print(s[i])
        pal1 = palindrome(s, i, i)
        pal2 = palindrome(s, i, i+1)
        length = max(pal1, pal2)
        if length > (end - start + 1):
            print('length', length)
            print('i', i)
            start = i - (length - 1)//2
            end = i + length//2
            print('start, end', start, end)
        i += 1
    return s[start:end + 1]
    
def palindrome(s, left, right):
    if len(s) ==0 or left > right:
        return 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    print('left right', left, right)
    return right - left - 1


s = "babad"
p = longestPalindrome(s)
print('\nLongset palindrome in {} is {}'.format(s, p))
