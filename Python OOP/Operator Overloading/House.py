class House:

    def __init__(self,d,w):
        self.window=w
        self.door=d


    def __add__(self,other):

        obj=House((self.door+other.door),(self.window+other.window))
        return obj 
    def view(self):
        print("The house has:",self.door,"doors and",self.window,"windows")
    
# Tester part

h1=House(2,4)
h2=House(3,6)
h3=h1+h2
h3.view()