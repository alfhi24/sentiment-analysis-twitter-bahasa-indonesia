import tweepy
from textblob import TextBlob
from tweepy import OAuthHandler
import twitter_auth # CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = OAuthHandler(twitter_auth.CONSUMER_KEY, twitter_auth.CONSUMER_SECRET)
auth.set_access_token(twitter_auth.ACCESS_TOKEN, twitter_auth.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

jml = 20
tweets = api.search(q=['papua', 'mahasiswa'], count = jml)

sum_polarity = 0
for tweet in tweets : 
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    hasil = analysis.translate(from_lang = 'id', to = 'en')
    print(hasil.sentiment, "/n")
    sum_polarity += hasil.polarity

value = sum_polarity / jml

if (value > 0) :
    print(value, " ", "Positive")
elif (value == 0) : 
    print(value, " ", "Netral")
else  :
    print(value, " ", "Negative")
