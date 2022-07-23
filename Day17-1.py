# create a class
class User:
    # pass
    def __init__(self, user_id, username):
        print("new user being created.")
        self.id = user_id
        self.username = username
        self.followers = 0


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
print(user_two.username)
print(user_one.followers)
