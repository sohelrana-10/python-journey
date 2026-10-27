from abc import ABC,abstractmethod

class Food(ABC):
    @abstractmethod
    def taste(self):
        pass
class Pizza(Food):

    def size(self):
        print("12' pizza.")
    def taste(self):
        print("Pizza is amazing.")
    
#Tester part

p=Pizza()
p.size()
p.taste()