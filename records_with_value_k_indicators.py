test_list = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]
print("The original list is : " + str(test_list))
ele = 3
k = 1
res = []
for x, y, z in test_list:
	if y == ele:
		res.append((x, y, z))
print("The tuples of element at kth position : " + str(res))