class Student:

    def __init__(self,Name,ID):
        self.Name=Name
        self.ID=ID
        self.Dept="CSE"
    def show_details(self):
        print("Student Name:",self.Name,"Student ID:",self.ID,"Departement:",self.Dept)
    
    @classmethod
    def from_string(cls,input_string):
        name,id=input_string.split(",")
        obj=cls(name,id)
        return obj

#Tester Part
stu=Student("Sohel Rana",573)
stu1=Student.from_string("Meher,100")
stu1.show_details()
