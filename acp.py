class Dog:
    animal = "dog"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def display(self):
        print("animal:",Dog.animal)
        print("breed:",self.breed)
        print("name:",self.name)
        print()

dog1 = Dog("labrador","buddy")
dog2 = Dog("german shephered","rocky")

dog1.display()
dog2.display()