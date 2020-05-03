# create classes for social account
# they have a field for: name, friends
# they have methods to: count_friends, befriend, unfriend


class SocialAccount(object):
    def __init__(self, name):
        self.name = name
        self.friends = []                   # list of SocialAccounts

    def count_friends(self):
        return len(self.friends)            # get length of list, number of elements in list

    def befriend(self, friend_name):
        self.friends.append(friend_name)

    def unfriend(self, friend_name):
        self.friends.remove(friend_name)

    def __str__(self):
        return self.name                    # damit werden die namen der freunde aufgelistet

    def __repr__(self):
        pass




michael = SocialAccount("Michael")
elisabeth = SocialAccount("Elisabeth")
christian = SocialAccount("Christian")
patrick = SocialAccount("Patrick")

michael.befriend(elisabeth)
michael.befriend(christian)
michael.befriend(patrick)
print(michael.count_friends())

for friend in michael.friends:
    print(friend)