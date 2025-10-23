print(
    '''
    **************************
    * Encapsulation Examples *
    **************************
    '''
)
class Student:
    def __init__(self,name):
        self.name=name
        self.__grade=0
    def set_grade(self,grade):
        if 0<=grade<=100:
            self.__grade=grade
        else:
            print("Grades are Between 0 and 100")
    def get_grade(self):
        return self.__grade
    def get_status(self):
        if self.__grade>=60:
            print("Passed")
        else:
            print("Failed")

na=input("Enter the Name of the Student : ")
gra=int(input("Enter the Grade of the Student : "))

obj=Student(na)
obj.set_grade(gra)
print(obj.get_grade())
obj.get_status()
