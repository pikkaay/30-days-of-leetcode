'''
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively.
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.
You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
'''


# dyamic programming - memoization

weight = [5, 6, 7, 8, 9, 10, 20, 25, 30]
value = [60, 65, 70, 75, 80, 85, 100, 110, 120]
W = 50

count = 1
memo = []

def knapsack(wt, val, w, n):
	try:
		if memo[n]:
			print('memo')
			return memo[n]
	except:
		pass

	if n == 0 or w == 0:
		result = 0
		# return result

	elif wt[n - 1] <= w:
		global count
		print(count)
		count += 1
		result =  max(val[n - 1] + knapsack(wt, val, w - wt[n - 1], n - 1),
					knapsack(wt, val, w, n - 1))
	else:
		result = knapsack(wt, val, w, n - 1)
	memo.append(result)
	return result

out = knapsack(weight, value, W, len(weight))
print(out)
