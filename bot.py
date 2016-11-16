import praw
import time
import datetime
import slackweb

r = praw.Reddit(user_agent = "/r/Futurology/ scraper by aniskhan001")
s = slackweb.Slack(url="https://hooks.slack.com/services/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")

cache = []

def run_bot():
	the_time = time.mktime( datetime.datetime.utcnow().timetuple() )
	submissions = r.get_subreddit('Futurology').get_hot()

	for sub in submissions:
		# The Top post is over 15 hours old OR less than 750 upvotes
		if ( the_time - sub.created_utc > 54000 or sub.score < 750):
			if sub.id in cache:
				continue
			else:
				cache.append(sub.id)
				hour_diff = int( (the_time-sub.created_utc)/3600 )
				s.notify(text = sub.title + "\nThere's an open position on /r/Futurology! The top post has " + str(sub.score) + " points and was posted " + str( hour_diff ) + " hours ago.")

while True:
	run_bot()
	s.notify(text = 'Sleep time')
	time.sleep(1*60) # 2 minutes call interval