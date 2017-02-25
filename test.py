from twython import Twython # pip install twython
import time # standard lib

''' Go to https://apps.twitter.com/ to register your app to get your api keys '''
CONSUMER_KEY = 'ttuTy4LgTuW7BfybbfFSRI8HE'
CONSUMER_SECRET = 'Bke8lbeuOt7Z9Z9ImDKX1tn9fkp3FIE6tuWukhVw7J5XFOQIav'
ACCESS_KEY = '27943545-rVkdyiotfSoLasgedKBYOzdnJj1l07q0LoeeBTbDU'
ACCESS_SECRET = 'lhEwOTjBirFbcLUkDKcBeN86RgZug1FGzh0Hw82corgQJ'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
lis = [467020906049835008] ## this is the latest starting tweet id
for i in range(0, 16): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="Quasi___",
    count=200, include_retweets=False, max_id=lis[-1])
    time.sleep(300) ## 5 minute rest between api calls

    for tweet in user_timeline:
        print(tweet['text']) ## print the tweet
        lis.append(tweet['id']) ## append tweet id's
