import tweepy
import time
import random
import datetime
import logging
import schedule
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

twitter_API = tweepy.API(auth)
followers = twitter_API.followers()
Timeline = twitter_API.home_timeline(count=5)

unique_tweet_code = ''

places = ["Krodent", "Murder Kroger", "UNT Campus", "Denton", "TWU Campus",
          "Denton County", "the Square", "Downtown", "Boca 31", "District 1",
          "District 2", "District 3", "Recycled Books", "District 4", "Fred Moore Park",
          "Quakertown Park", "Barley & Board", "South Lakes Park", "North Lakes Park",
          "Rayzor Ranch", "Idiot's Hill", "City Hall", "The Courthouse Lawn", "Clear Creek Nature Preserve",
          "University Lanes", "Wiggly Field Dog Park", "Emily Fowler Central Library",
          "North Branch Library", "South Branch Library", "The Golden Triangle Mall",
          "West Oak Coffee", "Dark Age Tattoo Studio", "The MLK Rec Center", "The Civic Center Pool"]

people = ["Fake Mayor, Gerard", "The Bonsai Lady", "Deb Armintor",
          "Keely Briggs", "Paul Meltzer", "The Terrible Scott Brown",
          "Sparky Pearson", "Jason Lee", "Neal Smatresk", "Big Tony", "The Albino Squirrel",
          "Downtown Preacher", "Flat Earth Guy", "Bubbles", "Animal Head Keyboard Guy",
          "Lovely Ronald", "A Mean Real Estate Lady", "An Aggressive Squirrel", "Little Emilio",
          "Guiseppe", "Frenchy", "The Denton Spiderman", "The Awful Jack Bell",
          "Chris Watts", "Brandon Chase McGee", "The Bonsai Lady"]

verbs = ["jumping", "screaming", "laughing", "gaming",
         "whispering", "yelling", "nodding", "running", "walking",
         "clapping", "punching", "kicking", "karate-chopping", "eating", "jogging",
         "sitting", "growling", "crawling", "squatting", "t-posing", "baking",
         "singing", "thrashing", "dancing", "fishing", "lollygagging", "jump-roping",
         "pitching a musical", "doing some influencer-type stuff", "t-posing"]

issues = ["Lovecraftian-horror", "squirrel-infestation", "dimensional vortex",
          "glowing glyphs", "ghosts", "corporeal goatman", "Garfield cult",
          "soggy spaghetti", "annoying Kyle kid", "the vaping enthusiasts",
          "animated inanimate objects", "spontaneous breaking out into song"]

bad_things = ["misogyny", "racism", "rudeness", "apathy", "hateful rhetoric",
              "mis-use of of City property", "landlords", "shady dealings",
              "crimes committed with pizzas", "squirrel-taming", "local feuds",
              "abuse of City funds", "tax evasion", "morally ambiguous land deals",
              "Robeson Ranch Political Participation"]


def unique_tweet_id():
    global unique_tweet_code
    code = random.randint(0, 999) + random.randint(0, 999) + random.randint(0, 999)
    unique_tweet_code = str(code)
    return unique_tweet_code


def public_tweet():
    unique_tweet_id()
    if datetime.date.today().weekday() == 0:
        tweet_to_publish = "Good day citizens, today is Monday and I saw " + people[random.randint(0, len(people))] + \
                           " " + verbs[random.randint(0, len(verbs))] + " with " + \
                           people[random.randint(0, len(people))] + ". Unique tweet code: " + unique_tweet_code
        # Monday morning tweet
    if datetime.date.today().weekday() == 1:
        tweet_to_publish = "Good day citizens, today is Tuesday and I saw " + people[random.randint(0, len(people))] + \
                           " " + verbs[random.randint(0, len(verbs))] + " at " + \
                           places[random.randint(0, len(places))] + ". Unique tweet code: " + unique_tweet_code
        # Tuesday morning tweet
    if datetime.date.today().weekday() == 2:
        tweet_to_publish = "Good day citizens, today is Wednesday and I legislated a fix to the " + \
                           issues[random.randint(0, len(issues))] + " issue " + "at " + \
                           places[random.randint(0, len(places))] + ". Unique tweet code: " + unique_tweet_code
        # Wed morning tweet
    if datetime.date.today().weekday() == 3:
        tweet_to_publish = "Good day citizens, today is Thursday and I had an interesting conversation with " + \
                           people[random.randint(0, len(people))] + " at " + places[random.randint(0, len(places))] + \
                           " about " + verbs[random.randint(0, len(verbs))] + ". Unique tweet code: " + unique_tweet_code
        # Thursday morning tweet
    if datetime.date.today().weekday() == 4:
        tweet_to_publish = "Good day citizens, today is Friday and I will be instituting policy to prevent " + \
                           people[random.randint(0, len(people))] + " from " + verbs[random.randint(0, len(verbs))] + \
                           " at " + places[random.randint(0, len(places))] + ". Unique tweet code: " + unique_tweet_code
        # Friday morning tweet
    if datetime.date.today().weekday() == 5:
        tweet_to_publish = "Good day citizens, today is Saturday and I am having a nice little rest at " + \
                           places[random.randint(0, len(places))] + ". Unique tweet code: " + unique_tweet_code
        # Saturday morning tweet
    if datetime.date.today().weekday() == 6:
        tweet_to_publish = "Good day citizens, today is Sunday and I am having a nice little rest by " + \
                           verbs[random.randint(0, len(verbs))] + " at " + places[random.randint(0, len(places))] + \
                           ". Excited to get back to work tomorrow!" + ". Unique tweet code: " + unique_tweet_code
        # Sunday
    twitter_API.update_status(tweet_to_publish)


def after_work_tweet():
    unique_tweet_id()
    if datetime.date.today().weekday() == 0:
        tweet_to_publish = "Another successful Monday of governing, today I eradicated " + \
                           str(random.randint(2, 15)) + " instances of " + \
                           bad_things[random.randint(0, len(bad_things))] + \
                           ". Errors deleted, entering sleep mode. Good night citizens!" + ". Unique tweet code: " + unique_tweet_code
        # after work tweet Mon
    if datetime.date.today().weekday() == 1:
        tweet_to_publish = "Another successful Tuesday of governing, today I eradicated " + \
                           str(random.randint(2, 15)) + " instances of " + \
                           bad_things[random.randint(0, len(bad_things))] + \
                           ". Errors deleted, entering sleep mode. Good night citizens!" + ". Unique tweet code: " + unique_tweet_code
        # after work tweet Tue
    if datetime.date.today().weekday() == 2:
        tweet_to_publish = "Another successful Wednesday of governing, today I eradicated " + \
                           str(random.randint(2, 15)) + " instances of " + \
                           bad_things[random.randint(0, len(bad_things))] + \
                           ". Errors deleted, entering sleep mode. Good night citizens!" + ". Unique tweet code: " + unique_tweet_code
        # after work tweet Wed
    if datetime.date.today().weekday() == 3:
        tweet_to_publish = "Another successful Thursday of governing, today I eradicated " + \
                           str(random.randint(2, 15)) + " instances of " + \
                           bad_things[random.randint(0, len(bad_things))] + \
                           ". Errors deleted, entering sleep mode. Good night citizens!" + ". Unique tweet code: " + unique_tweet_code
        # after work tweet Thu
    if datetime.date.today().weekday() == 4:
        tweet_to_publish = "Another successful Friday of governing, today I eradicated " + \
                           str(random.randint(2, 15)) + " instances of " + \
                           bad_things[random.randint(0, len(bad_things))] + \
                           ". Errors deleted, entering sleep mode. Have a good weekend citizens!" + ". Unique tweet code: " + unique_tweet_code
        # after work tweet Fr
    if datetime.date.today().weekday() == 5:
        tweet_to_publish = "Another successful Saturday of relaxing. Entering sleep mode, good night citizens!" + ". Unique tweet code: " + unique_tweet_code
        # saturday and sunday equivalent
    if datetime.date.today().weekday() == 6:
        tweet_to_publish = "Another successful Sunday of relaxing. Entering sleep mode, good night citizens!" + ". Unique tweet code: " + unique_tweet_code
        # saturday and sunday equivalent
    twitter_API.update_status(tweet_to_publish)


def favorite():
    for tweet in Timeline:
        if tweet.user.screen_name != "MayorRobo":
            try:
                print('\nRoboMayor found cool tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to like it.')
                tweet.favorite()
                print('Tweet liked successfully.')
                time.sleep(10)
            except tweepy.TweepError as error:
                print("\nError. Favorite not successful. Reason: ")
                print(error.reason)
            except StopIteration:
                break


def public_retweet():
    for tweet in Timeline:
        if tweet.user.screen_name != "MayorRobo":
            try:
                print('\nRoboMayor found cool tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')
                tweet.retweet()
                print('Tweet retweeted successfully.')
                time.sleep(10)
            except tweepy.TweepError as error:
                print("\nError. Retweet not successful. Reason: ")
                print(error.reason)
            except StopIteration:
                break


def check_mentions(api, keywords, since_id):
    logging.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logging.info(f"Answering to {tweet.user.name}")
            unique_tweet_id()

            if not tweet.user.following:
                tweet.user.follow()

            api.update_status(
                status="Interesting human-brained thought, entering into governing algorithms to check for compatibility. Unique tweet code: " + unique_tweet_code,
                in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True
            )
    return new_since_id


def twitter_bot():
    public_tweet()
    public_retweet()
    favorite()
    after_work_tweet()


def main():
    schedule.every().day.at("17:30").do(twitter_bot)
    since_id = 1
    while True:
        since_id = check_mentions(twitter_API, ["will you please"], since_id)
        logging.info("Waiting...")
        time.sleep(60)
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()



