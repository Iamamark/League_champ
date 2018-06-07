import praw
import league_champ_spells

reddit = praw.Reddit(client_id = 'EFqhniHnnpHxrw',
                       client_secret = 'asC_3YxGOKpalDCcMjH0u9KKZgk',
                       username = 'ChampAbilitiesBot',
                       password = 'platbtw',
                       user_agent = 'A Champion Ability Bot for r/summonerschool')

subreddit = reddit.subreddit('summonerschool')
submissions = subreddit.hot(limit = 5)

for post in submissions:
    if not post.stickied:
        post.comments.replace_more(limit = 0)
        comments = post.comments.list()
        for comment in comments:
            print(comment.body)

