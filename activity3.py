print("select your ride")
print("1. bike")
print("2. car")


choice = int(input("enter your choice: "))

if( choice == 1 ):   #condition 1 outer if statement
    print("what type of bike? ")
    print("scooty/n")
    print("scooter/n")

    choice2=int(input("enter your choice2: "))
    if choice2==1: 
        print("you have selected scooty")
    else:
        print("you have selected scooter")

elif(choice == 2 ):
          print("what type of car?")
          print("1.sedan")
          print("2.xuv")
          choice3=int(input("enter your choice3"))
          if choice3==1:
                
             print("you have selected sedan")
          else:
               print("you have selected xuv")
else:
     print("wrong choice")
               

