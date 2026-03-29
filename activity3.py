#take marks as input from user
print("enter marks obtained in 4 subjects: ")
history = int(input("history :"))
english = int(input("english :"))
science = int(input("science :"))
bengali = int(input("bengali :"))

#lets calculate the perc of marks
sum = history+english+science+bengali
print("sum of history,english,science and bengali")

perc = (sum/400)*100

print("percentage mark = ",perc)