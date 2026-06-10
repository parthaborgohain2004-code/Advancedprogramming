class Address:
    def __init__(self, street, city, zipCode):
        self.street = street
        self.city = city
        self.zipCode = zipCode

    def __str__(self):
        return f"{self.street}, {self.city} - {self.zipCode}"


class Student:
    def __init__(self, name, age, address, courses=None):
        self.name = name
        self._age = None
        self.age = age
        self.address = address
        self.courses = courses if courses is not None else []

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0 or value > 120:
            raise ValueError("Age must be a valid positive integer (1-120).")
        self._age = value

    def add_course(self, course):
        self.courses.append(course)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Courses: {', '.join(self.courses) if self.courses else 'None'}")


class ScholarshipStudent(Student):
    def __init__(self, name, age, address, courses=None, scholarshipAmount=0):
        super().__init__(name, age, address, courses)
        self.scholarshipAmount = scholarshipAmount

    def display(self):
        super().display()
        print(f"Scholarship Amount: ₹{self.scholarshipAmount}")


if __name__ == "__main__":
    addr = Address("MG Road", "Guwahati", "781001")

    s1 = Student("Rahul", 20, addr)
    s1.add_course("Math")
    s1.add_course("Physics")

    print("---- Student ----")
    s1.display()

    s2 = ScholarshipStudent("Anita", 22, addr, ["Biology"], 50000)

    print("\n---- Scholarship Student ----")
    s2.display()