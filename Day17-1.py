# create a class
class User:
    # pass
    def __init__(self, user_id, username):
        print("new user being created.")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # adding methods to a class
    def follow(self, user):
        user.followers += 1
        self.following += 1


# create an object
user_one = User("100", "Mitra")

# create an attribute
# user_one.id = "001"
# user_one.username = "Mitra"

# print(user_one.username)
print(user_one.id)

# user_two = User()
# user_two.id = "002"
# user_two.username = "Mina"
user_two = User("002", "Mina")
# print(user_two.username)
# print(user_one.followers)
user_one.follow(user_two)
print(user_one.followers)
print(user_one.following)
print(user_two.followers)
print(user_two.following)

user_two.follow(user_one)
print(user_one.followers)
print(user_one.following)
print(user_two.followers)
print(user_two.following)
