#Assigning subsequent rows to Matrix first row elements
#Using dictionary comprehension
#initializing list
test_list = [[5,8,9], [2,0,9], [5,4,2],[2,3,9]]
#printing original list
print("The original list: " + str(test_list))
#pairing each 1st col with next rows in matrix
res = {test_list[0][ele] : test_list[ele + 1] for ele in range(len(test_list)-1)}
#printing result 
print("The Assigned Matrix : " + str(res))
res = dict(zip(test_list[0], test_list[1:]))
