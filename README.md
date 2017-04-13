# loscampsbot
A Twitter bot that tweets lyrics from Los Campesinos! songs, available at [@loscampsbot](https://twitter.com/loscampsbot).

## Why
I was bored, I'm a great fan of Los Campesinos! and I wanted to do a Twitter bot. Basically.

## How
I created a new account for the bot and obtained the necessary keys and tokens. I used tweepy to connect with the Twitter API to post the status updates. The bot itself is dead simple: it gets a random line from the lyrics.txt file, it checks if these lyrics fit in a tweet (all of them should but oversights can happen) and that it isn't empty, and then posts it. After 20 minutes, the process starts again. The bot is deployed on Heroku.

## What

- lyrics.txt: the file where all the lyrics are written. I got them from [Genius](https://genius.com/artists/Los-campesinos) and edited them slightly (removing repetitions of the chorus, writing some lyrics two times but in different combinations). Roughly by inverse release order, if anyone wants to check. Bars (|) are used to mark where the new line characters will go, replacing them in the script itself.
- Procfile: declares the process type and the command to be run by the dyno on Heroku.
- requirements.txt: requirements and dependencies for the script.
- tweet.py: the script for the bot. Written in Python 2.7. Uses tweepy to access the Twitter API and linereader to easily grab a line from the lyrics file.
