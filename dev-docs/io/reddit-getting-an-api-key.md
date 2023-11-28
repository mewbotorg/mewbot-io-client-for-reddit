
Before you can do anything with reddit, you need to generate an API key.

This is slightly more involved that it has to be.

1) Sign up for reddit.

You're going to need a basic account before proceeding further.

2) Generate a bot id and secret

You're going to need this later when it comes time to tell reddit about your bot.
Since reddit tightened up on granting tokens, you need to actually ask them on an individual basis to authorize your bot.

Read

https://praw.readthedocs.io/en/stable/getting_started/authentication.html

first.

Then go to 

https://www.reddit.com/prefs/apps

3) Choose a script app

This form of app actually gives you a script and a secret which you can use in the script.

To retrieve your secret and id at a later date, go to 

https://www.reddit.com/prefs/apps

4) Register your app

I'm not really sure that I filled out the form right...

https://reddithelp.com/hc/en-us/requests/new?ticket_form_id=14868593862164

Guess we'll see if the credentials start working.

5) They did - you need to add your username and password to the yaml - as well as a subreddit to watch.

But it worked.

