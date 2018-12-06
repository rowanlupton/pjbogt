from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
from config import HANDLE, follow, listenFor, responses
import tweepy
import json, random, re

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def on_error(self, status_code):
        print('status_code: ', status_code)
        api.send_direct_message(user_id=rowanlupton, text="pjbogt is down")
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return True
        else:
            # this doesn't actually work so it's commented out until tweepy
            # updates for the new twitter api

            # api.send_direct_message(screen_name='rowanlupton', text="pjbogt is down")
            print('pjbogt failed with status_code: ', status_code)
    def on_status(self, status):
        if status.user.id_str in follow:
            if not hasattr(status, 'retweeted_status'):
                api.update_status(random.choice(responses), in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)


streamListener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=streamListener)
stream.filter(follow=follow, async=True)

api.update_status("*slaps roof of alex goldman* this bad boy can fit so many weird flexes")
