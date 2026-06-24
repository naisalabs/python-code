set1 = set(map(int, input("enter elemnts of set 1 separated by spaces: "
    ).split()))

set2 = set(map(int, input("enter elemnts of set 2 separated by spaces: "
    ).split()))

result = set1.symmetric_difference(set2)

print("symmetric Different:", result)