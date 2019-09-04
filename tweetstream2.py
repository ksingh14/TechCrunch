from tweepy import Stream
from tweepy.streaming import StreamListener
 
import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'jN1bb414O1jWMx1WqkkcZrODx'
consumer_secret = 'Ttc8FVMiZo80A6Zgkf1xb0yLeXZlvQwY1KTX6ssH9AZ7itvVo7'
access_token = '860622290-F0xFVdi98DsDFqN0h0VMnZjdD7ORiEDWXFulL8nj'
access_secret = 'Ob82vesOcUdVBkIbpYfsGuDefyYEmp9yhyB44H8Mu0nXq'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print 'fuck'
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#kunalsingh'])