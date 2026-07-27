#import packages
from abc import ABC, abstractmethod
#create a base cls
class animal(ABC):
    #abc method
    #should be implemented by all sub-classes
    def move(self):
        pass
#sub classes
class human(animal):
    def move(self):
        print("i can walk and run")
class snake(animal):
    def move(self):
        print("i caan crawl")
class dog(animal):
    def move(self):
        print("i can bark")
class lion(animal):
    def move(self):
        print("i can roar")
# driver code
R = human()
R.move()

k = snake()
k.move()

R = dog()
R.move()

k = lion()
k.move()