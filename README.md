# twitter-bot
This is a simple twitter bot which keeps saving tweets related to a keyword and retweet them after analyzing...

## MySQL Setup :
1) ```mysql -u "root" -p```
2) *type your password* leave blank if using for first time...
3) create DATABASE twitter;
4) use twitter;
5) CREATE TABLE tweets (tid VARCHAR(30), tweet VARCHAR(300));
6) quit

## Other settings in settings.py
1) change your Database usernam, password in that file.
2) go to https://apps.twitter.com/ and add a new app.
3) now get credential for your app.
4) Put that in settings.py

## Python module installation
1) ```pip install tweepy```
2) ```pip install mysql-python```

## Running your Setup
1) Run Listening.py
```python Listening.py```
It will save tweets which contains your keywords in it in your database;

*** You can do analysys and see which tweets needs to be retweeted and which not....***

2) Run Retweeting.py
```python Retweeting.py```
It will retweet your tweets and delete them after retweeting
