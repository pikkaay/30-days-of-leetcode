'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

def groupAnagrams(strs):

	# sorted
	strs_sorted = []
	for i in range(len(strs)):
		strs_sorted.append(''.join(sorted(strs[i])))

	print(strs_sorted)
	ht = dict()
	for i in range(len(strs_sorted)):
		
		if strs_sorted[i] in ht:
			ht[strs_sorted[i]].append(strs[i])
		else:
			ht[strs_sorted[i]] = [strs[i]]
	print(ht)
	ls = []
	for i in ht.values():
		ls.append(i)
	print(ls)
	return  ls


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(strs)

'''
['aet', 'aet', 'ant', 'aet', 'ant', 'abt']
{'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

'''
