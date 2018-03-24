import tweepy, MySQLdb

Database_ip = "localhost"
Database_user = "pandey"
Password = ""
Database_name="twitter"

conn = MySQLdb.connect(Database_ip, Database_user, Password, Database_name)
c = conn.cursor()
conn.set_character_set('utf8')

ckey="***SBBDXsXYRHlloCdrH66***"
csecret="***6x853MsQdd0dob9Kgw70wPShWy5iLM***"
atoken="****C5W5Epe7m5G1G5MVRDB8Cq4V7clo****"
asecret="****1aSpQZ40dkT1VPQdDF6UlkmA9ARs3Q***"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

keyword = "test"
