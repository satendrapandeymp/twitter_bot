from tweepy import Stream
from tweepy.streaming import StreamListener
from settings import c, api, conn, auth, keyword
import json, sys

reload(sys)
sys.setdefaultencoding('utf-8')

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
	try:
		tweet = all_data["text"]
		tid = all_data["id_str"]

		c.execute("INSERT INTO tweets (tid, tweet) VALUES (%s,%s)",(tid, tweet))
		conn.commit()

		print((tweet))

	except KeyError:
	    pass

    def on_error(self, status):
        print status

twitterStream = Stream(auth, listener())
twitterStream.filter(track=[keyword])
