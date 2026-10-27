class Student:

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show_details(self):
        print("Student Name:",self.name,"Student ID:",self.id)

class CSE_Student(Student):
    
    
    def do_lab(self):
        super().show_details()
        print("CSE Student do Lab Classes")

#Tester Part
Stu1=CSE_Student("Sohel Rana",573)
Stu1.show_details()
Stu1.do_lab()

Stu=Student("Meher",100)
Stu.show_details()
print(isinstance(Stu,Student))
print(isinstance(Stu1,Student))