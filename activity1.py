test_dict = {'codingal' : 1, 'is' : 1, 'best' :3, 'for' : 8, 'coding' : 1}
print("the original dictonary : " + str(test_dict))
K = 1
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print("frequency of K is: " + str(res))