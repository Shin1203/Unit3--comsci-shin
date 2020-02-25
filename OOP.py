#
# What’s a class?
# What’s an instance?
# What’s the relationship between a class and an instance?
What’s the Python syntax used for defining a new class?
What’s the spelling convention for a class name?
How do you instantiate, or create an instance of, a class?
How do you access the attributes and behaviors of a class instance?
What’s a method?
What’s the purpose of self?
What’s the purpose of the __init__ method?
Describe how inheritance helps prevent code duplication.
Can child classes override properties of their parents?
#



```
# practising object structure based on worksheet
class Dogs:
    # class atributes
    species = 'mammal'

    # self. defines intial state of attribute, self.name is an attribute with default as name
    # these are instance properties
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    pass


def get_biggest_age(*args):
    biggest = max(args)
    print(f"the biggest is {biggest}")


a = Dogs('pepe', 3)
b = Dogs('bobo', 1)
c = Dogs('momo', 5)

get_biggest_age(a.age, b.age, c.age)

print(a.age)
a.birthday()
print(a.age)


# you can create "child" classes that inherit the parent class's attributes and behaviors.
# parent class
class Cat:
    # class attribute
    species = "mammal"

    # initializer/ instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


# child class (inherits from Cat class)
class BritishShorthair(Cat):
    def run(self, speed):
        return f"{self.name} runs {speed}"


class PersianCat(Cat):
    def run(self, speed):
        return f"{self.name} runs {speed}"


krat = BritishShorthair("Krat", 12)
print(krat.description())
print(krat.run("slowly"))


```
