import requests
import random
import tweepy
import time

print('PyCats started : ')

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'
res1 = ['&width=960&height=540','&width=1280&height=720']
urls = 'https://loremflickr.com/api/1/?token='+random.choice(res1)+'&tag=cat,cats'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    time.sleep(10)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        response = requests.get(urls)
        file = open('test.jpg','wb')
        file.write(response.content)
        file.close
        file = open('test.jpg', 'rb')
        reponse = api.media_upload(filename='test.jpg', file=file)
        print(reponse)
        media_ids = [reponse.media_id_string]
        print(media_ids)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#cat' in mention.full_text.lower():
            print(str(mention.id) + ' ' + mention.user.screen_name + ' - ' + mention.full_text)
            print('Test trouve')
            print('Reponse..')

            api.update_status(media_ids=media_ids, status='@'+mention.user.screen_name+' '+'hop '+'@'+mention.user.screen_name, in_reply_to_status_id=mention.id)
        file.close

while True:
    reply_to_tweets()
    time.sleep(15)
