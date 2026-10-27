class Student:

    def __init__(self,name,id):
        self.__name=name
        self.__id=id
        

    def student_details(self):
        print("Student Name:",self.__name,",Student ID:",self.__id)
    
    def update_ID(self,id):
        if id>0:
            self.__id=id
        else:
            print("Invalid ID.Enter a valid ID.")

#Tester part

Stu=Student("Sohel Rana",573)
Stu.student_details() 

Stu.__name="Afrin" #This will create a new variable
Stu.student_details()

print(Stu.__dict__)
Stu.update_ID(543)
Stu.student_details()