# creating attribute
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0
# creating methods
    def follow(self, user):
        user.follower += 1
        user.following += 1
        
user_1 = User("1", "Ashish")
user_2 = User("2", "Komal")

user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)




