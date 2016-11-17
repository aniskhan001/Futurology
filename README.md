# SubReddit 2 Slack

Grab submissions from **/r/`your-submission`/** and post directly to your Slack channel.

#### This script uses:
* [PRAW](https://praw.readthedocs.io/en/stable/) `pip install praw`
* [slack-python-webhook](https://github.com/satoshi03/slack-python-webhook) `pip install slackweb`

## How to use?
* Create / Sign in to your Slack team
* Create a new [incoming webhook](https://my.slack.com/services/new/incoming-webhook) and choose a desired channel
* Set the url to `WEBHOOK_URL` environment variable. You can use the .env file with `key=value` pair combination
* Finally run `python bot.py`


This particular repo is raedy for heroku deployment also.

Feel free to contribute any time! Cheers!
