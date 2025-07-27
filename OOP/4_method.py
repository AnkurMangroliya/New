class Youtube:
    def __init__(self, username, subscribers=0, subscription=0):
        self.username = username
        self.subscribers = subscribers
        self.subscription = subscription

    def subscribe(self, user):
        user.subscribers += 1
        self.subscription += 1

user1 = Youtube("Tech Guru")
user2 = Youtube("Code Master")
user1.subscribe(user2)
print(f"User 1 subscribers: {user1.subscribers}")
print(f"User 1 subscription: {user1.subscription}")
print(f"User 2 subscribers: {user2.subscribers}")
print(f"User 2 subscribers: {user2.subscription}")

