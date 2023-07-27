import instaloader
ig=instaloader.Instaloader()
dp=input("Enter Username :")
ig.download_profile(dp,profile_pic_only=True)
profile=instaloader.Profile.from_username(ig.context,dp)
allposts=profile.get_posts()
for post in allposts:
    ig.download_post(post,dp)
    break
print("Successfully Downloaded Profile pic and Latest post")