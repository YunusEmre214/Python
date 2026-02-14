class Student:
    count=0
    total_gpa=0

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
        Student.total_gpa+=gpa
    
    #Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students:{cls.count}"
    @classmethod
    def get_gpa(cls):
        if cls.count==0:
            return 0
        else:
            return f"Total # of students Gpa:{cls.total_gpa/cls.count}"
student1=Student("Spongebob",3.2)
student2=Student("Mark",2.8)
student3=Student("Eva",3.7)
print(Student.get_count())
print(Student.get_gpa())