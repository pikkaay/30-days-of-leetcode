'''
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively.
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.
You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
'''

# recursion

weight = [5, 6, 7, 8, 9, 10, 20, 25, 30]
value = [60, 65, 70, 75, 80, 85, 100, 110, 120]
W = 50

count = 1

def knapsack(wt, val, w, n):
	# print(n)
	if n == 0 or w == 0:
		return 0

	if wt[n - 1] <= w:
		global count
		print(count)
		count += 1
		return max(val[n - 1] + knapsack(wt, val, w - wt[n - 1], n - 1),
					knapsack(wt, val, w, n - 1))
	else:
		return knapsack(wt, val, w, n - 1)


out = knapsack(weight, value, W, len(weight))
print(out)
