import praw
import time

r = praw.Reddit(user_agent = "/r/Futurology/ scraper by aniskhan001")

cache = []
subs = []

def run_bot():
	the_time = time.time()
	submissions = r.get_subreddit('Futurology').get_hot()

	for sub in submissions:
		# The Top post is over 15 hours old OR less than 750 upvotes
		if ( the_time - sub.created > 54000 or sub.score < 750):
			if sub.id in cache:
				continue
			else:
				cache.append(sub.id)
				print sub.id
				print sub.url
				# print sub.title

while True:
	run_bot()
	print 'Time to sleep!'
	time.sleep(30*60) # 30 minutes call interval