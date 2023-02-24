# RoboMayor

Running bot is @MayorRobo on twitter!

Twitter bot that acts like the town mayor primarily using functionalities from the Tweepy API.

Scheduled to on a daily basis look at the past 5 tweets in its timeline, retweet and favorite them, and then create two
unique tweets each day based on a dictionary of terms mad libs style.

Activated by the phrase "will you please" which when tweeted at the RoboMayor will cause it to follow that user and respond
with a generic message.


Files needed to run:

Procfile - This gives instruction to a server platform if you want to host the program to keep it running continuosly.
main.py - This is the main program file for the app that contains all the Python code on which it runs.
runtime.txt - This simply specifies which version of Python the platform that is running the app should use.
requirements.txt - These are the required modules/libraries needed to run the app. NOTE: These are overkill as they currently are written in the file and contain unrelated modules that the app does not actually need in order to run.


You will need to set up a Twitter account and provide your own Twitter Developer API keys for that account in order for this to be able to authenticate to Twitter and run.
