# A class is like a blueprint for creating objects. An object has properties and methods
#(function) associated with it. almost everythin in python is object

# create class
class User:
     # Constructor
     def __init__(self,name,email,age):
         self.name = name
         self.email = email
         self.age = age

     def greeting(self):
         return f"My name is {self.name}, i am {self.age}, and my email is {self.email} "
      
    # Init user object
harsh = User("Harsh Dwivedi", "harsh@gmail.com", 17)

print(harsh.greeting())
