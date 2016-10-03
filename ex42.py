class Animal(object):
    def __init__(self, gender):
        self.gender = gender

class Dog(Animal):
    def __init__(self, name, gender):
        self.name = name
        super(Dog, self).__init__(gender)

class Cat(Animal):
    def __init__(self, name, gender):
        self.name = name
        super(Cat, self).__init__(gender)

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.pet = None

class Employee(Person):
    def __init__(self, name, gender, salary):
        super(Employee, self).__init__(name, gender)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover", "Male")
satan = Cat("Satan", "Female")
mary = Person("Mary", "Female")
mary.pet = satan
print satan.gender

frank = Employee("Frank", "Male", 120000)
frank.pet = rover

flipper = Fish()
crouse = Salmon()
harry = Halibut()