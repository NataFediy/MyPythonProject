#! Time Delta
# When users post an update on social media, such as a URL, image,
# status update etc., other users in their network are able to view
# this new post on their news feed. Users can also see exactly when
# the post was published, i.e, how many hours, minutes or seconds ago.
#
# Since sometimes posts are published and viewed in different time zones,
# this can be confusing. You are given two timestamps of one such post that
# a user can see on his newsfeed in the following format:
# Day dd Mon yyyy hh:mm:ss +xxxx
# Here +xxxx represents the time zone.
#
# Task: Your task is to print the absolute difference (in seconds)
# between them.
#
# Input Format:
# The first line contains T, the number of test cases.
# Each test case contains 2 lines, representing time t1 and time t2.
#
# Output Format:
# Print the absolute difference (t2 - t1) in seconds.
#
# Sample Input:
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
# Sample Output:
# 25200
# 88200
#
# Explanation:
# In the first query, when we compare the time in UTC for both the time
# stamps, we see a difference of 7 hours. which is 7*3600 seconds or
# 25200 seconds.
# Similarly, in the second query, time difference is 5 hours and 30 minutes
# for time zone adjusting for that we have a difference of 1 day and
# 30 minutes. Or 24*3600+30*60 = 88200

# !/bin/python3
import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    print(t1, t2,sep='\n')
    return int(abs((t2 - t1).total_seconds()))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    print(t)

    for _ in range(t+1):
        t1 = datetime.datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
        t2 = datetime.datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
        time_delta(t1, t2)
        delta = str(time_delta(t1, t2))
        print(delta)
        # fptr.write(delta + '\n')

    # fptr.close()
