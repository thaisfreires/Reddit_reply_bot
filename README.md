### Reddit reply bot

This Python script acts as a Reddit bot, responding to new submissions within the specified subreddit. It's configured to issue a maximum of 10 replies and prints a message while processing.

### Requirements

Python3
Reddit account
Reddit App credentials (configuration below)
[PRAW] (https://praw.readthedocs.io/en/stable/getting_started/installation.html)(Python Reddit API Wrapper) to interact with Reddit's API.

### Usage

> python3 reddit_bot.py
Insert your Reddit credentials on the code
Define the subreddit you want your bot to work on (default subreddit = "pythonforengineers")
Define your trigger words and reply text (default trigger_word = "test", reply_text = "another test")


### Reddit App Account configuration

- Log in your Reddit account 
- [Enter this page] (https://www.reddit.com/prefs/apps/)
- Click the *Create an app* button 

name: your bot name 
type: choose *script*
description: optional
about url: optional
redirect uri: http://localhost:8080

- *create app*, and note the client_id (under *personal use script*) and client_secret. 
> [!NOTE]
> Do not share this information. Those are your Reddit credentials.
