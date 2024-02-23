import praw
import time

client_id = "" 
client_secret = "" 
username = "" 
password = "" 
user_agent = "" 

# Initialize Reddit API client
reddit = praw.Reddit(client_id="your client_id",  
                     client_secret="your client_secret",  
                     username="your username",  
                     password="your reddit password", 
                     user_agent="a name for your bot e.g "Comment python bot 0.1"")  

# Subreddit to target
subreddit = reddit.subreddit("pythonforengineers")
# Submissions to limit
submission_count = 0
# Phrase to trigger the bot 
trigger_word = "test"

# Check every submission in the subreddit 
for submission in subreddit.stream.submissions(): 
    if trigger_word in submission.title:
        # Initialize the reply text 
        reply_text = "another test" 
        submission.reply(reply_text)
        # Print each title to reply
        print(f"Replying to: {submission.title}")

        # Count the submissions and stop after 10
        submission_count += 1
        if submission_count >= 10:
           break

        if submission_count % 5 == 0:
           # Sleep for a specified duration to avoid rate limiting
           time.sleep(1)
        