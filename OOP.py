
# What’s a class?
# A class is a user-defined data structure that can store information

# What’s an instance?
# An instance of a class has stored variables- the class is the structure and the instance a variable in that structure. 

# What’s the relationship between a class and an instance?
# An instance is made out of a class, the class defines all the properties it's instances can have

# What’s the Python syntax used for defining a new class?
 class x:
        def __init__(self, y, z, m):
            self.y = y
            self.z = z
            self.m = m
 pass
    
# What’s the spelling convention for a class name?
# capitalize first letter, e.g- Dog, Cat, Milk

# How do you instantiate, or create an instance of, a class?
instance = classname(argument properties)

# How do you access the attributes and behaviors of a class instance?
instance.attribute
instance.behavior(argument of function)

# What’s a method?
# functions inside of a class that define the behaviours of the objects

# What’s the purpose of self?
# self is an instance of the class, it is used so that instances of a class can have different variables. if you put Classname.attribute, 
#the variable is a class attribute, not an instance attribute- A.k.a all instances of the class will have the same attribute.

# What’s the purpose of the __init__ method?
# initializes object's initial attributes

# Describe how inheritance helps prevent code duplication.
# if you wanted to make classes that had some similarities but some differences, you dont have to make complete differnt classes, but put
# them under a parent class that stores their similarities, so that you don't have to rewrite the similarities.

# Can child classes override properties of their parents?
# yes.



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
