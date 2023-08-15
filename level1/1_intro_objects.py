"""
We a building a object Type : COunter

Attributes
Number -> Inter Tye

Methods:
    Count -> incerement the number by 1 everytime an event occurs\

Atriibutes consist of names and values

Methods can accept input and interact with objects attributes
calling a method is how we run the code within

"""
class Counter: # how we define an object type
    # a class is a blueprint for creating a specific type of object
    def __init__(self): # special method called constructor
        self.number = 0 #attribute name


    def count(self): # method name count
        self.number+=1