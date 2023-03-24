#!/bin/python

# pip install snscrape
import snscrape.modules.twitter as sntwit
import csv

# Specify the name of the output file
output_file = 'tweet_data.csv'
# Specify the query parameters
query = "Breast Cancer AND LGBT since:2022-10-01 until:2022-10-31"

# Make the request to Twitter
tweets=sntwit.TwitterSearchScraper(query).get_items()

# Populate a list with the data
tweetdatas = []
for i,tweet in enumerate(tweets):
  #tweetdata = [tweet.date, tweet.id, tweet.user.username, tweet.rawContent]
  tweetdata = [tweet.date, tweet.user.location, tweet.user.username, tweet.user.id, tweet.user.displayname, tweet.user.verified, tweet.user.url, tweet.retweetCount, tweet.likeCount, tweet.rawContent, tweet.url]

  tweetdatas.append(tweetdata)


# Save out the tweet data
with open(output_file, mode='w', newline='') as csv_file:
  writer = csv.writer(csv_file)

  # write the header row
  #writer.writerow(['Date', 'ID', 'Username', 'Content'])
  writer.writerow(['Date', 'location', 'user_name', 'user_ID', 'user_handle', 'ticks', 'user_url', 'retweet_number', 'like_number', 'tweet_content', 'tweet_url'])

  # write the data rows
  for tweetdata in tweetdatas:
    writer.writerow(tweetdata)
