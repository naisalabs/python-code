class myclass:

    # private var
    _privatevar = 27;
    
    #private method
    def __priMeth(self):
        print("i am inside class myClass")

    def hello(self):
        print("private varieble value: ",myclass.__privatevar)


foo = myclass()
foo.hello()
foo._priMeth