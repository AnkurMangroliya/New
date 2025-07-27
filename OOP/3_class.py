class StarCokkie:
    milk = "almond milk" # Class attribute
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    
star_cokkie1 = StarCokkie("red", 50)
star_cokkie2 = StarCokkie("blue", 60)
print(star_cokkie1.milk)
print(star_cokkie2.milk)
print(StarCokkie.milk)  # Output: almond milk

print(star_cokkie1.__dict__)  # Output: {'color': 'red', 'weight': 50}  # Output: Tech Guru
print(star_cokkie2.__dict__)  # Output: {'color': 'blue', 'weight': 60}
print(StarCokkie.__dict__)  # Output: {'__module__': '__main__', 'milk': 'almond milk', '__init__': <function StarCokkie.__init__ at 0x...>, '__dict__': <attribute '__dict__' of 'StarCokkie' objects>, '__weakref__': <attribute '__weakref__' of 'StarCokkie' objects>, '__doc__': None}

# we externally defined the milk attribute to object, it does not change the class attribute.

star_cokkie1.milk = "soy milk"
print(star_cokkie1.__dict__)  # Output: {'color': 'red', 'weight': 50}  # Output: Tech Guru
print(star_cokkie2.__dict__)  # Output: {'color': 'blue', 'weight': 60}
print(StarCokkie.__dict__)


# if you change the class attribute, it will change for all instances of the class.
# If you change the instance attribute, it will only change for that specific instance.

