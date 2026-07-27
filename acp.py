#import necessary modules
from abc import ABC, abstractmethod
#create base cls
class ABsclass(ABC):
    # funtion to print a value
    def print(self,x):
        print("passed value: ",x)
    # abstract method
    @abstractmethod
    def task(self):
        print("we are inside ABclass task")
# create sub cls
class test_class(ABsclass):
    def task(self):
        print("we are inside test_class task")
#obj of test_cls created
test_obj = test_class()
test_obj.task()
test_obj.print(100)