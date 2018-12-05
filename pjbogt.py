from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
from config import HANDLE, listenFor, noRT, responses
import tweepy
import random, re

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return True
        else:
            api.send_direct_message(screen_name=rowanlupton, text="pjbogt is down")
    def on_status(self, status):
        statusText = status.text
        
        if not hasattr(status, 'retweeted_status'):
            api.update_status(random.choice(responses), in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)

streamListener = StreamListener()
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
stream.filter(track=listenFor, async=True)

# api.update_status("no, they're really not")
