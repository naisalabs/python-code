# take input for the student that he ca attend the exam or not
medical_cause = input("did you have a medical cause (y/n):").strip(). upper()


if medical_cause == 'Y':   # condition 1
   print("you're allowed")
else:
   
   atten = int(input("enter the attendence of the student: "))

   if atten >= 75:   #condition 2
       print("you're allowed")
   else:
        print("you're not allowed")