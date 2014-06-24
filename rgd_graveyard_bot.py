__author__ = 'Anthony Nelson'

import praw, re


def test_comments(sub):
    #included = True
    r = re.compile('http')
    for comment in sub.comments:
        if (comment.author != sub.author and
            comment.author != '[deleted]' and
            r.search(comment.body)):
            return False

    return True


r = praw.Reddit(user_agent='graveyard_bot')

r.login('rgd_graveyard_bot','password')
thelist = []
for submission in r.get_subreddit('RedditGetsDrawn').get_new(limit=100,params={'after':'t3_28tisi'}):
    if submission.author == '[deleted]':
        continue

    if len(submission.comments) == 0:
        thelist.append(submission)
    elif test_comments(submission):
        thelist.append(submission)


c = 0
for item in thelist:
    c+=1
    print(str(c) + ' ' + item.permalink + ' ' + str(len(item.comments)) + ' comments')
