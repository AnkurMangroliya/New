class StarCookie:
    def __init__(self):
        print("Creating a star cookie!")


star_cookie = StarCookie()
star_cookie.name = "Chocolate Chip"
star_cookie.size = "Large"
print(star_cookie.name)  # Output: Chocolate Chip

# Here attributes are liek variables that associated with the object star_cookie.


star_cookie2 = StarCookie()
star_cookie2.name = "Oatmeal Raisin"
star_cookie2.size = "Medium"
print(star_cookie2.name)  # Output: Oatmeal Raisin
print(star_cookie2.size)  # Output: Medium



# Every time we have to difine the attributes for each object, which can be tedious.
# We can use the __init__ method to initialize attributes when creating an object.


# This works same as the above code.
class StarCookie1:
    def __init__(self, color):
        self.color = color

star_cookie1 = StarCookie1("Red")
print(star_cookie1.color)  # Output: Red


# Insert new line
print("\n")

# set of default attributes
class Youtube:
    def __init__(self, channel_name, subscribers=0):
        self.channel_name = channel_name
        self.subscribers = subscribers

user1 = Youtube("Tech Guru")
print(user1.subscribers)



