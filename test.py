import discord
import os
import sys
import random
import asyncio
import time
import praw
import requests
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta
from utils.data import getJSON

config = getJSON("config.json")

footer = config.footerembed
start_time = time.monotonic()

reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    user_agent=config.user_agent,
    username=config.username,
    password=config.password,
)


def is_url_image(image_url, psubmissions):
    image_formats = ("image/png", "image/jpeg", "image/jpg", "image/gif", "image/gifv")
    r = requests.head(image_url)
    if r.headers["content-type"] in image_formats:
        urlvar = image_url
        return urlvar
    else:
        submission = psubmissions[random.randint(1, 50) - 1]
        is_url_image(submission, psubmissions)


def redditgrabber(subreddit, amount: int = None, time: str = None):
    description = None
    urlvar = None
    subreddit = subreddit.replace("r/", "")

    submissions = []

    if not amount:
        amount = 50
    if not time:
        time = "month"

    for submission in reddit.subreddit(subreddit).top(time, limit=amount):
        if (
            submission and not submission.stickied and not submission.over_18
        ):  # if submission is NOT pinned or NSFW
            submissions.append(submission)

    submission = submissions[random.randint(1, 50) - 1]

    if not submission.is_self:
        urlvar = is_url_image(submission.url, submissions)
    elif submission.is_self:
        description = submission.selftext

    return {
        "title": submission.title,
        "url": f"https://reddit.com{submission.permalink}",
        "upvotes": submission.score,
        "imgurl": urlvar,
        "desc": description,
        "comments": submission.num_comments,
    }


test = redditgrabber("r/dankmemes")
print(test["url"])
