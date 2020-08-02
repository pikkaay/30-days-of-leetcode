'''
fibonacci series
'''

# Recursive 
# Time complexity O(2^n)
def fibonacci(n):
	if n == 1 or n == 2:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))



# Dynamic Progrmming
# Time complexity O(n^2)
memo = [0]
def fibonacci(n):
	try:
		if memo[n]:
			return memo[n]
	except:
		pass
	if n == 1 or n == 2:
		result = 1
	else:
		result = fibonacci(n-1) + fibonacci(n-2)
	memo.append(result)
	return result


print(fibonacci(1000))
