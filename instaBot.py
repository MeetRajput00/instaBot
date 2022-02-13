from instapy import InstaPy

usr=input("Enter the username: ")
pwd=input("Enter the password: ")
session = InstaPy(username=usr,password=pwd)
session.login()
session.set_do_story(enabled = True, percentage = 100, simulate = True)
def followUserFollowing():
    user=input("Enter the username of account: ")
    n=int(input("Enter amount of following: "))
    session.follow_user_following(user, amount=n, randomize=True)

def likePostsByTags():
        # Like posts based on hashtags
    tags=input("Enter the tag: ")
    n=int(input("Enter the amount of posts: "))
    session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
    session.like_by_tags(tags, amount=n)

def likePostsOnYourFeed():
    n=int(input("Enter amount of posts: "))
    session.like_by_feed(amount=n, randomize=True, interact=True)

def followByTags():
    tags=input("Enter tag: ")
    n=int(input("Enter amount of following: "))
    session.follow_by_tags(tags, amount=n, interact=True)

def followUserFollowers():
    friend=input("Enter the username: ")
    n=int(input("Enter amount of followers: "))
    session.follow_user_followers(friend, amount=n, randomize=False, interact=True)

def followLikers():
    friend=input("Enter the username: ")
    n=int(input("Enter amount of followers: "))
    session.follow_likers(friend, photos_grab_amount = 2, follow_likers_per_photo = n, randomize=True, sleep_delay=600, interact=False)

def unfollowWhoDontFollow():
    n=int(input("Enter amount of people: "))
    session.unfollow_users(amount=n, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)

def interactWithSomeone():
    comment=input("Enter comment: ")
    user=input("Enter the username: ")
    n=int(input("Enter amount of posts: "))
    session.set_comments(comment)
    session.set_do_comment(enabled=True, percentage=100)
    session.set_do_like(True, percentage=70)
    session.interact_by_users(user, amount=n, randomize=True, media='Photo')

def watchStories():
    user=input("Enter username: ")
    session.story_by_users(user)

print("Enter 1 to like posts by tags")
print("Enter 2 to like posts on your feeds")
print("Enter 3 to follow by tags")
print("Enter 4 to follow by user's following")
print("Enter 5 to following user's followers")
print("Enter 6 to follow likers of photos")
print("Enter 7 to unfollow people who don't follow you back")
print("Enter 8 to interact with specific user")
print("Enter 9 to watch someone's stories")
print("Enter 0 to exit")
choice=1
while(choice!=0):
    choice=int(input("Choose: "))
    if choice is 1:
        likePostsByTags()
    elif choice is 2:
        likePostsOnYourFeed()
    elif choice is 3:
        followByTags()
    elif choice is 4:
        followUserFollowing()
    elif choice is 5:
        followUserFollowers()
    elif choice is 6:
        followLikers()
    elif choice is 7:
        unfollowWhoDontFollow()
    elif choice is 8:
        interactWithSomeone()
    elif choice is 9:
        watchStories()
    else:
        choice=0


