import tweepy, MySQLdb, json, time, sys
from settings import c, api, conn

reload(sys)
sys.setdefaultencoding('utf-8')

delete = []
test = c.execute("select * from tweets")
print test

for i in range(test):
	row = c.fetchone()
	tid = str(row[0])
	delete.append(tid)
	print "Reading " + tid

for tid in delete:
	api.retweet(tid)
	c.execute("delete from tweets where tid = {0}".format(tid))
	print "Deleting " + tid

conn.commit()
