#taking total amount as input from user
amount =int(input("pls enter amount for withraw:"))

#calculating the number of notes of different denominations
note_1 = amount//200
note_2= (amount%100)//50
note_3 = ((amount%100)%50)//10


print("notes if 200 taka" ,note_1)
print("notes of 50 taka" , note_2)
print("notes of 10 taka" , note_3)