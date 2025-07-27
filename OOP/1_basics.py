# Object oriented programming basics

# what is method and attribute?
# A method is a function that is defined inside a class and can operate on instances of that class. -> like what housekeeper can do
# An attribute is a variable that is associated with an instance of a class.   -> like what housekeeper has

# what is class and object?
# A class is a blueprint for creating objects. It defines the properties and behaviors that the objects created from the class will have.
# An object is an instance of a class. It is created from the class and has its own unique state and behavior.

# class Housekeeper:
# objects = Merry and Jane which are instances of Housekeeper class means they are housekeepers.

# Identity, attributes, and behavior
# Identity refers to the unique identifier of an object, which is typically its memory address.
# Attributes are the data that an object holds, while behavior refers to the methods that an object can perform.
# behavior is defined by the methods of the class, which can manipulate the object's attributes or perform actions related to the object.

# Object definition
# robot_a = RobotBlueprint()

# Empty class
class StarCokkie:
    pass    

star_cokkie = StarCokkie()
print(type(star_cokkie))  # Output: <class '__main__.StarCokkie'>