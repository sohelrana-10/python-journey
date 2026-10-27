class Student:
    university_name="NUB"

    def __init__(self,name,id):
        self.name=name 
        self.id=id

    def show_details(self):
        print("Student Name:",self.name,"Student ID:",self.id,"University Name:",Student.university_name)

    @classmethod
    def update_Uni_name(cls,new_name):
        if new_name !=None and new_name.strip()!="":
            cls.university_name=new_name
        else:
            print("Enter valid University name.")

#Tester part
Stu=Student("Sohel Rana",573)  
Stu.show_details()
Student.update_Uni_name("    ")
Stu.show_details()