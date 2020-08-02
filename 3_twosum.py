'''
two sum problem
'''

A = [1, 2, 3, 4, 5, 6]
k = 10

bruteforce
lookup = set()
for i in range(len(A)):
	for j in range(len(A)):
		if i != j:
			if A[i] + A[j] == k:
				# print(A[i], A[j])
				lookup.update([A[i], A[j]])
print(lookup)








# Hashtable
A = [1, 2, 3, 4, 5, 6]
k = 10

lookup = set()
for i in range(len(A)):
	lookup.add(A[i])

print(lookup)
for i in range(len(A)):
	if k - A[i] in lookup and k - A[i] != A[i]:
		print(A[i])
