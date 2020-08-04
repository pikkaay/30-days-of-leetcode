'''
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


S = 'abcqabcdbb'

ht = set()

start_index = 0
current_pointer = 1
length = 1


ht.add(S[start_index])
for i in range(1, len(S)):
	if S[i] in ht:
		ht.remove(S[i])
		ht.add(S[i])
	else:
		ht.add(S[i])
	
	if len(ht) > length:
		length = len(ht)


print(S)
print(ht)
print(length)
