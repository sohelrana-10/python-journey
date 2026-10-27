class A:

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show_details(self):
        print("Student Name:",self.name,"Student ID:",self.id)    
class B:

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show_details(self):
        print("Student Name:",self.name,"Student ID:",self.id)

class C(A,B):
    def __init__(self,name,id):
        self.name=name
        self.id=id
        B.show_details(self)
    
    # def show_details(self):
    #     print("Student Name:",self.name,"Student ID:",self.id)

c=C("Sohel Rana",573)
c.show_details()
