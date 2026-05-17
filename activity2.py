valid = False
while not valid:
    try:
        n=int(input("enter you number: "))
        #enter a even  number
        while n%2==0:
          valid = True
    except ValueError:
      print("invalid")
