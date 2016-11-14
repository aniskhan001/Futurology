import time
import datetime

# date = datetime.datetime.now().total_seconds()

# d1 = date.timetuple()

# # datetime.datetime.fromtimestamp( second )
# print datetime.datetime.fromtimestamp(1478947122) # UTC - current time
# print datetime.datetime.fromtimestamp(1478893122) # UTC - 15 Hrs ago (54000 seconds)

dang = time.time()
print datetime.datetime.now()
print dang
print datetime.datetime.fromtimestamp( dang )
print datetime.datetime.fromtimestamp( dang - 54000 )