# class Point:

# def print_Point(p):
# print(f"({p.x} + {p.y})")


# blank = Point()
# blank.x = 3.0
# blank.y = 4.0


# print(blank.y)
# print(blank.x)

# print(f"({blank.x} + {blank.y})")
# print(blank)

# white = point()
# white.id = "00.1"
# print(white)

class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return f"{self.name} sings {song}"

    def dance(self):
        return f"{self.name} is dancing"


blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
print(f"Blu is a {blu.__class__.species}")
print(f"Woo is a {woo.__class__.species}")
# print(f"{Parrot(name=blu)} is {Parrot(age=15)}")
print(f"{blu.name} is {blu.age} years old.")
print(blu.sing("happy"))
print(blu.dance())

