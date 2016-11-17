import praw
import time
import datetime
import slackweb
from os import environ


####################
### user options ###
####################

cache = []
the_limit = 3 # how many top submissions (max) per call, reddit default order
call_interval = 10 # time interval to run the bot again, in minutes
the_subreddit = 'Futurology' # your chosen subreddit

# An user agent is important. Change according to your needs.
r = praw.Reddit(user_agent = "/r/" + the_subreddit + "/ scraper by aniskhan001")
# it's a good practice to save the WEBHOOK_URL in an environment variable so we don't expose the URL
s = slackweb.Slack(url = environ.get('WEBHOOK_URL'))


######################
### bot definition ###
######################

def run_bot():

	the_time = time.mktime( datetime.datetime.utcnow().timetuple() )
	submissions = r.get_subreddit(the_subreddit).get_hot(limit = the_limit)

	for sub in submissions:
		"""
		A sample logic is added. You can always build your own logic
		For accessing different members of PRAW object, the /sample_data file is given as reference

		"""

		# The Top post is over 15 hours old OR less than 750 upvotes | 15*60*60 = 54000 seconds
		if ( (the_time - sub.created_utc > 54000 or sub.score < 750) and (sub.id not in cache) ):

			# cahing the item so we don't post it twice
			cache.append(sub.id)
			hour_diff = int( (the_time - sub.created_utc) / 3600 )

			# Learn more about messaging format: https://api.slack.com/docs/message-formatting
			message_text = "There's a new post on <"+ sub.permalink +"|/r/" + the_subreddit + "!> posted *" + str(hour_diff) + " hours* ago with: *" + str(sub.score) + "* upvotes!"
			s.notify(text = message_text)


while True:
	run_bot()
	time.sleep(call_interval*60)