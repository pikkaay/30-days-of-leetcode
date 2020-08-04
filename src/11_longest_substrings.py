'''
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


# s = 'pwwkew'

# ht = set()

# start_index = 0
# current_pointer = 1
# length = 1


# ht.add(s[start_index])
# for i in range(1, len(s)):
# 	print(ht)

# 	if s[i] in ht:
# 		print('remve add')
# 		ht.remove(s[i])
# 		ht.add(s[i])
# 	else:
# 		print('add')
# 		ht.add(s[i])
	
# 	if len(ht) > length:
# 		length = len(ht)






# print(s)
# print(ht)
# print(length)


'''

'''



s = 'pwwkew'

ht = set()

a = 0
b = 0
length = 1

while b < len(s):
	if not s[b] in ht:
		print('adding', s[b])
		ht.add(s[b])
		b += 1
		length = max(len(ht), length)
	else:
		print('remving and adding ', s[a])
		ht.remove(s[a])
		b += 1
		a += 1
		


print(s)
print(ht)
print(length)
