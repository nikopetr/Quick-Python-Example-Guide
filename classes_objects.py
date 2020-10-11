from datetime import date  # Importing date in order to get the current date


# Classes and objects

# The "self" in Python classes: self represents the instance of the class. By using the “self” keyword we can access
# the attributes and methods of the class in python. It binds the attributes with the given arguments. The reason you
# need to use self is because Python does not use the @ syntax to refer to instance attributes. Python decided to do
# methods in a way that makes the instance to which the method belongs be passed automatically, but not received
# automatically: the first parameter of methods is the instance the method is called on
class Person:
    # init method / constructor
    def __init__(self, name, age):
        # The "_" on _name shows that this is a private variable and doesn't change from the outside without going
        # through one the methods
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    # Self is a convention and not a real python keyword.
    # self is parameter in function and you can actually use another parameter name
    # in place of it. But it is advisable to use self because it increases the readability of the code.
    def get_age(in_place_of_self):
        return in_place_of_self._age

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def __str__(self):
        return "Person:\n  Name: " + self._name + ", Age: " + str(self._age)

    # a method-function to create a CV object by the Person's object details.
    def create_cv(self):
        return CV(self)

    # a static method-function (notice there is no self as a parameter-argument)
    @staticmethod
    def calculate_age_difference(person1, person2):
        if isinstance(person1, Person) and isinstance(person1, Person):
            return abs(person1.get_age() - person2.get_age())
        else:
            return "The parameters given were not instances of Person"

    # Different constructor - a class method to create a Person object by birth year.
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)


class CV:
    # init method / constructor
    def __init__(self, person):
        if isinstance(person, Person):
            self._details = str(person)

    def __str__(self):
        return "CV: " + self._details


# Creates an object of the class Person with my name and age
me = Person("Nick", 22)
print(me)

# Creates an object of the class Person with my name and age by calculating the difference of years since my birth year
me2 = Person.from_birth_year("Nick", 1998)
print(me2)

my_brother = Person("Leo", 16)

# In order to find the age difference of me and my brother
print(Person.calculate_age_difference(16, me))  # This should not work since 16 is not an instance of Person
print(Person.calculate_age_difference(my_brother, me))  # This should work and print 6'

# Creates an object of CV from the instance me
my_cv = me.create_cv()
print(my_cv)