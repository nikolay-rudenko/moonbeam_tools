import tweepy
import time

auth = tweepy.OAuthHandler('FiJjjPX7OqsARpbE1vcN37VLa', 'Zd3wUM2YnxgTz4rUuUKHBpQsFkUeJT4Rs96q099KpNQIrIqfVR')
auth.set_access_token('428090162-23dBJoGhB4eYJMiKXUZJtJTWVSeEQXStvTE6FwzX',
                      'OpoB9cxVkeZPy19ARARj2xQZhIWWRwI04VSuebrv6qOPb')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except StopIteration:
        return

search_string = 'I love python'
numbers_of_tweets = 1

for tweet in tweepy.Cursor(api.search, search_string).items(numbers_of_tweets):
    try:
        tweet.retweet()
        # tweet.favorite()
        print('I love that tweet! ')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break



# Bot that could follow back people on twitter
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'Olga C':
#         print(follower.name)
#         follower.follow()

