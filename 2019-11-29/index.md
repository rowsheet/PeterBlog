# 2019-11-29
# Everything you need to know about Python:

## Object-Oriented Classes

Python is a typical object-oriented language.

In Python, you can create `Class` objects, inherit from them, and do all sorts of stuff. But defining methods and classes in Python has some gotchas. Here's a typical contrived use case; we'll run this code and explain what it's doing after.

There are three files:

1. main.py
2. animal.py
3. dog.py
4. cat.py

(Yes, it's the stupid animal example. This document is intended to show you the syntax of Python, not the nuances of OOP).

File: `main.py`

    from dog import Dog
    from cat import Cat
    
    def log_main_event(msg):
        print("""\
    --------------------------------------------------------
    %s
    --------------------------------------------------------
        """ % msg.upper())
    
    if __name__ == "__main__":
    
        log_main_event("initialize characters...")
    
        doggo = Dog(given_name="Doggo",age=4)
        doggo.print_info()
        business_cat = Cat(given_name="Business Cat", age=1000)
        business_cat.print_info()
    
        log_main_event("make characters do things...")
    
        doggo.mark_territory()
        business_cat.get_hungry()

Here's a super contrived main function. It does two things:

1. Initialize characters
2. Make characters do things

### 1. Initialize characters

Firstly, the main function initializes class objects `Dog` and `Cat`. Looking at the `Dog` class, we can see that it has a [constructor](https://en.wikipedia.org/wiki/Constructor_%28object-oriented_programming%29) that takes `given_name` and the `age` of the dog. In Python, constructors are the `__init__` method of a class. Note that all methods of a class in python have `self` as the first parameter, no matter the other parameters.

    from animal import Animal
    
    class Dog(Animal):
    
        def __init__(self, given_name=None, age=None):
            super().__init__(**{
                "given_name": given_name,
                "age": age,
                "animal_type": "Dog",
                "scientific_name": "Canis lupus familiaris",
                "greeting": "Woof!"
            })
    
        def mark_territory(self):
            print("> Calling dog.mark_territory()...\n")
            self.greet()
            print("**%s is peeing on your lawn...\n" % self.given_name)

In `dog.py`, the Dog constructor calls it's base class (the class that it extends). We can see on line 3 of `dog.py` that Dog extends Animal. Looking at Dog's constructor, we can see that it calls it's base constructor with `kwargs`. Looking at Animal's constructor, we can see it's a `**kwarg` method that internally looks for the parameters:

 - `given_name`
 - `age`
 - `animal_type`
 - `scientific_name`
 - `greeting`

Since only `given_name` and `age` are set by user (or anyone initializing an Dog), all the other variables are already pre-set in Dog's constructor to be set for it's base Animal constructor. There's no need for a user to specify the `greeting` , `animal_type`, or `scientific_name` when initializing a Dog.

This is an example of how we abstract an implementation of Animal with the interface that is Dog's constructor. Here is the definition of Animal:

    class Animal:
    
        def __init__(self, **kwargs):
            self.animal_type = kwargs["animal_type"]
            self.scientific_name = kwargs["scientific_name"]
            self.given_name = kwargs["given_name"]
            self.age = kwargs["age"]
            self.greeting = kwargs["greeting"]
            print("Initializing a new %s..." % self.animal_type)
    
        def print_info(self):
            info = """\
        Animal Type:        %(animal_type)s
        Scientific Name:    %(scientific_name)s
        Given Name:         %(animal_type)s
        Age:                %(age)s
        Greeting:           %(greeting)s
            """ % {
                "animal_type": self.animal_type,
                "scientific_name": self.scientific_name,
                "animal_type": self.animal_type,
                "age": self.age,
                "greeting": self.greeting,
            }
            print(info)
    
        def greet(self):
            print("%(animal_type)s says:     %(greeting)s" % {
                "animal_type": self.animal_type,
                "greeting": self.greeting,
            })
    
        def poke(self):
            print("Poking %(animal_type)s..." % {
                "animal_type": self.animal_type,
            })
            self.greet()

As you can see, Animal is a more complex object with a more complex constructor (or `__init__` method). Animal has some abstract classes with objects extending it can use, such as `print_info()`.

Note that this class could also be initialized by a user. There's nothing preventing a user for initializing a new Animal instance and providing all of the 5 required variables in a verbose constructor.

Extending the class allows us to write a cleaner interface to commonly used parameters.

### 1. Make characters do things

Once we initialize the characters we can interact with them by calling either abstract methods of methods defined in the extended class.

In this case, the only methods defined in extended classes are:

    doggo.mark_territory()
    business_cat.get_hungry()

## Takeaways:

1. Python extends base classes in the definition of the class (in parentheses).
2. All methods of a class object must have `self` as the first parameter.
3. Calling a methods base constructor is done through `super().__init__([params])` and should be done in the extending classes constructor.
4. Python has no notion of **public**, **private**, or **protected** methods. Although it's convention to prepend methods that you'd prefer a class to be *private* with an underscore, there's nothing in Python's interpreter that enforces this.
5. If you want to prohibit and end-user from initializing an base class, you can make it an **[Abstract Base Class (ABC class)](https://docs.python.org/3/library/abc.html)** which is similar to Abstract classes in Java. This required the base class to extend `ABC` and for you to `from abc import ABC`.
