class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    
    
    def display_info(self):
        """Kişinin bilgilerini görüntüler"""
        print(f"Ad: {self.name}, Yaş: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  
        self.student_id = student_id  
    
    def display_info(self):
        """Öğrencinin bilgilerini görüntüler"""
        super().display_info()  
        print(f"Öğrenci No: {self.student_id}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age) 
        self.subject = subject  
    
    def display_info(self):
        """Öğretmenin bilgilerini görüntüler"""
        super().display_info() 
        print(f"Öğrettiği Ders: {self.subject}")


if __name__ == "__main__":
    # Person (Kişi) nesnesi
    person = Person("Melike", 35)
    print("Kişi Bilgisi:")
    person.display_info()
    
    # Student (Öğrenci) nesnesi
    student = Student("Berk", 19, "S54321")
    print("\nÖğrenci Bilgisi:")
    student.display_info()
    
    # Teacher (Öğretmen) nesnesi
    teacher = Teacher("Fatma", 42, "Kimya")
    print("\nÖğretmen Bilgisi:")
    teacher.display_info()
