import time
import datetime

# date = datetime.datetime.now().total_seconds()

# d1 = date.timetuple()

# # datetime.datetime.fromtimestamp( second )
# print datetime.datetime.fromtimestamp(1478947122) # UTC - current time
# print datetime.datetime.fromtimestamp(1478893122) # UTC - 15 Hrs ago (54000 seconds)

# dang = time.time()
# print datetime.datetime.now()
# print dang
# print datetime.datetime.fromtimestamp( dang )
# print datetime.datetime.fromtimestamp( dang - 54000 )

# print datetime.datetime.fromtimestamp( 1479297780.81 )
# print datetime.datetime.fromtimestamp( 1479276180.81 )
# print datetime.datetime.fromtimestamp( 1479246866.0 )
# print datetime.datetime.fromtimestamp( 1479275666.0 )

the_time = time.time()
print the_time

if (time.timezone > 0):
	the_time -= time.timezone
else:
	the_time += time.timezone

print the_time

print datetime.datetime.fromtimestamp ( time.mktime(datetime.datetime.utcnow().timetuple()) )