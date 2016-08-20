class Animal(object):
    """Animal is-an Object"""
    pass

class Dog(Animal):
    """Dog is-an Animal"""
    def __init__(self, name):
        """Dog has-a name"""
        self.name = name

class Cat(Animal):
    """Cat is-an Animal"""
    def __init__(self, name):
        self.name = name


class Person(object):
    """person is-an object"""
    def __init__(self, name):
        self.name = name
        ## person has-a pet
        self.pet = None

class Employee(Person):
    """Emplyee is-a Person"""
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Whale(Fish):
    pass


person = Person("test", 120000)
person.pet = Cat(self, "cat")
