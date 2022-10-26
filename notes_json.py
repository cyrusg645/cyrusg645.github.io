tweets_str = '''[
    {   "source": "Twitter Web Client", 
        "id_str": "6312794445", 
        "text": "Trump International Tower in Chicago ranked 6th tallest building in world by Council on Tall Buildings & Urban Habitat http://bit.ly/sqvQq", 
        "created_at": "Thu Dec 03 19:39:09 +0000 2009", 
        "retweet_count": 33,
        "favorite_count": 6
    },
    {   "source": "Twitter Web Client", 
        "id_str": "6971079756",
        "text": "From DONALD Trump: Wishing everyone a wonderful holiday & a happy, healthy, prosperous New Year. Let's think like champions in 2010!", 
        "created_at": "Wed Dec 23 17:38:18 +0000 2009",
        "retweet_count": 28,
        "favorite_count": 12
        
    }
]'''

import json
tweets = json.loads(tweets_str)
'''
with open('/Users/cyrus/Documents/GitHub/cyrusg645.github.io/condensed_2009 2.json', encoding='ascii') as f:
    text = f.read()
    text = text.encode('ascii')
    tweets = json.loads(text)
'''

paths = ['/Users/cyrus/Documents/GitHub/cyrusg645.github.io/condensed_2009 2.json']

num_tweets = 0
output_tweets = []
for tweet in tweets:
    print('inside for loop')
    print('tweet=',tweet)
    if 'trump' in tweet['text'].lower() and 'chicago' in tweet['text'].lower():
    #if 'Trump' in tweet['text'] or 'trump' in tweet['text']:
    #incorrect: if 'chicago' and ('trump' in tweet['text'].lower())
    #if ('chicago' and 'trump') in tweet['text'].lower():
        num_tweets += 1
        output_tweets.append(tweet)
print('num_tweets=',num_tweets)
print('len(tweets)=', len(tweets))

