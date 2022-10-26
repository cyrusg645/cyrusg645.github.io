#!/usr/bin/python3

'''
========================================
INSTRUCTIONS:
========================================

There are no pre-built functions and doctests for this lab.
This is to get you more experience writing entire python programs from scratch.

Step 1: Go to https://github.com/bpb27/trump_tweet_data_archive

Step 2: Download the files `condensed_*.json.zip`, where * is a year.
        There should be 10 total files (2009-2018).
        Trump has obviously sent tweets after 2018,
        but this particular archive of tweets has not been updated recently.

Step 3: Unzip each of these files to get files that look like `condensed_*.json`.

Step 4: Modify this `lab_part1.py` file so that it:

    1. Opens each json file and loads the file using the json library.
       Each file contains a list of tweets, and if you concatenate each file's tweets
       together you will get a list of all tweets ever sent by Donald Trump.

    2. Prints the total number of tweets.

    3. Counts the number of tweets that contain the following keywords:
       `Obama`, `Trump`, `Mexico`, `Russia`, and `Fake News`.
       It's important to remember that each of these words can appear with many different capitalizations, 
       and your program should count the word no matter how it is capitalized.  
       For example, `OBAMA`, `obama`, and `ObAmA` all need to count as an occurrence of the word `Obama`.

    4. Prints out a count of each of these words.

    My program gives the following output:

    ```
    len(tweets)= 36307
    counts= {'trump': 13924, 'russia': 412, 'obama': 2712, 'fake news': 333, 'mexico': 199}
    ```

    (Notice how I use markdown code-blocks from within python comments so you know exactly where my output starts/stops.
    It is very common to use markdown in python comments.)

    You'll know your program is correct if you get the same numbers.

Step 5: Select at least 3 more interesting words/phrases to count in trump's tweets.

Step 6: Calculate the percentage of tweets that contain each word.  (Both your new words and Trump's original tweets.)

Step 7: Display the results nicely.

    The display must have all words right justified and the percents printed with two 
    significant figures (on both sides of the decimal) as shown in the example output below.
    For example:

    ```
    percentage of tweets using phrase:
                  daca : 00.17
             fake news : 00.92
      mainstream media : 00.06
                mexico : 00.55
                 obama : 07.47
                russia : 01.13
                 trump : 38.35
                  wall : 00.91
    ```

    HINT:
    There are many ways to achieve this effect in python,
    but I recommend using the .format string function.
    Your python cheat sheet has instructions.

========================================
Submission
========================================

Upload your completed `lab_part1.py` file to sakai,
and copy and paste the output of running your program into sakai.
'''
import json


paths = ['/Users/cyrus/Documents/GitHub/cyrusg645.github.io/condensed_2009 2.json', '/Users/cyrus/Documents/GitHub/cyrusg645.github.io/condensed_2010.json', '/Users/cyrus/Documents/GitHub/cyrusg645.github.io/condensed_2011.json', '/Users/cyrus/Documents/GitHub/cyrusg645.github.io/condensed_2012.json', '/Users/cyrus/Documents/GitHub/cyrusg645.github.io/condensed_2013.json', '/Users/cyrus/Documents/GitHub/cyrusg645.github.io/condensed_2014.json', '/Users/cyrus/Documents/GitHub/cyrusg645.github.io/condensed_2015.json', '/Users/cyrus/Documents/GitHub/cyrusg645.github.io/condensed_2016.json', '/Users/cyrus/Documents/GitHub/cyrusg645.github.io/condensed_2017.json', '/Users/cyrus/Documents/GitHub/cyrusg645.github.io/condensed_2018.json' ]

tweets = []
for path in paths:
    with open(path, 'rb') as f:
        text = f.read()
        text = text.decode("ascii")
        tweets += json.loads(text)
print("len(tweets)=", len(tweets))

num_tweets = 0
numfakenews_tweets = 0
numtrump_tweets = 0
nummexico_tweets = 0
numobama_tweets = 0
numrussia_tweets = 0
numchina_tweets = 0
numjoe_tweets = 0
numhilary_tweets = 0

for tweet in tweets:
    
    if 'trump' in tweet['text'].lower():
        numtrump_tweets += 1
    if 'obama' in tweet['text'].lower():
        numobama_tweets += 1
    if 'mexico' in tweet['text'].lower():
        nummexico_tweets += 1
    if 'russia' in tweet['text'].lower():
        numrussia_tweets += 1
    if 'fake news' in tweet['text'].lower():
        numfakenews_tweets += 1
    if 'china' in tweet['text'].lower():
        numchina_tweets += 1
    if 'joe' in tweet['text'].lower():
        numjoe_tweets += 1
    if 'hilary' in tweet['text'].lower():
        numhilary_tweets += 1
print("numfakenews-tweets", numfakenews_tweets)
print("numtrump-tweets", numtrump_tweets)
print("nummexico-tweets", nummexico_tweets)
print("numobama-tweets", numobama_tweets)
print("numrussia-tweets", numrussia_tweets)
print("numchina-tweets", numchina_tweets)
print("numjoe-tweets", numjoe_tweets)
print("numhilary-tweets", numhilary_tweets)


print(f'''
percentage of tweets using phrase:
                trump  : {"{:05.2f}".format(numtrump_tweets/len(tweets)* 100)}
             fake news : {"{:05.2f}".format(numfakenews_tweets/len(tweets)* 100)}
                mexico : {"{:05.2f}".format(nummexico_tweets/len(tweets)* 100)}
                 obama : {"{:05.2f}".format(numobama_tweets/len(tweets)* 100)}
                russia : {"{:05.2f}".format(numrussia_tweets/len(tweets)* 100)}
                 china : {"{:05.2f}".format(numchina_tweets/len(tweets)* 100)}
                  joe  : {"{:05.2f}".format(numjoe_tweets/len(tweets)* 100)}
                hilary : {"{:05.2f}".format(numhilary_tweets/len(tweets)* 100)}
''')


