import json
import os
import requests
from sys import stderr
from flask import Flask, request, jsonify
import snscrape.modules.twitter as twitterScrapper
import json

app = Flask(__name__)

api_key = os.environ.get("API_KEY", "")
if api_key == "":
    print("api key is required", file=stderr)

api_base_url = "https://dev-bhagaskarash4zl.microgen.id/api" + api_key

@app.get("/products")
def handler():
    url="http://pmzmzxzinc.function.microgen.id/check"
    response = requests.get(url)
    return response.json()

@app.post("/hashtag")
def hashtag():
    try:
        print(request.data)
        posts = json.loads(request.data)
        limit = posts['limit']
        keyword = posts['keyword']

        tweets = []

        scraper = twitterScrapper.TwitterHashtagScraper(keyword)
        for i, tweet in enumerate(scraper.get_items()):
            if i > limit:
                break

            tweets.append({"id": tweet.id,
                           "username": tweet.user.username,
                           'content': tweet.content,
                           'url': tweet.url,
                           'date': tweet.date,
                           'renderedContent': tweet.renderedContent,
                           'replyCount': tweet.replyCount,
                           'retweetCount': tweet.retweetCount,
                           'likeCount': tweet.likeCount,
                           'quoteCount': tweet.quoteCount,
                           #    'conversationId': tweet.conversationId,
                           'source': tweet.source,
                           'sourceUrl': tweet.sourceUrl,
                           'sourceLabel': tweet.sourceLabel,
                           #    'outlinks': jsonify(tweet.outLinks),
                           #    'tcooutlinks': tweet.tcooutLinks,
                           'media': tweet.media,
                           #    'retweetedTweet': json.dumps(tweet.retweeetTweet),
                           #    'quotedTweet': tweet.quotedTweet,
                           'inReplyToTweetId': tweet.inReplyToTweetId,
                           #    'inReplyToUser': tweet.inReplyToUsers,
                           #    'mentionedUsers': tweet.mentionedUsers,
                           'coordinates': tweet.coordinates,
                           'place': tweet.place,
                           #    'hashtags': tweet.hastags,
                           'cashtags': tweet.cashtags,
                           #    'link': tweet.link,
                           #    'search': tweet.seacrh,
                           'likeCount': tweet.likeCount,
                           'retweetCount': tweet.retweetCount,
                           'lang': tweet.lang,
                           'searchBy': "HASHTAG"
                           })
        # j = json.dumps(tweets)
        return jsonify(tweets)
    except Exception as e:
        result = {
            "statusCode": 400,
            "error": e
        }
        return result
    
@app.post("/listpost")
def listpost():
    try:
        print(request.data)
        posts = json.loads(request.data)
        limit = posts['limit']
        keyword = posts['keyword']

        tweets = []

        scraper = twitterScrapper.TwitterListPostsScraper(keyword)
        for i, tweet in enumerate(scraper.get_items()):

            if i > limit:
                break
            print(f"{i} content: {tweet}")
            tweets.append({"id": tweet.id,
                           "username": tweet.user.username,
                           'content': tweet.content,
                           'url': tweet.url,
                           'date': tweet.date,
                           'renderedContent': tweet.renderedContent,
                           'replyCount': tweet.replyCount,
                           'retweetCount': tweet.retweetCount,
                           'likeCount': tweet.likeCount,
                           'quoteCount': tweet.quoteCount,
                           #    'conversationId': tweet.conversationId,
                           'source': tweet.source,
                           'sourceUrl': tweet.sourceUrl,
                           'sourceLabel': tweet.sourceLabel,
                           'sourceLabel': tweet.sourceLabel,
                           #    'outlinks': jsonify(tweet.outLinks),
                           #    'tcooutlinks': tweet.tcooutLinks,
                           'media': tweet.media,
                           #    'retweetedTweet': json.dumps(tweet.retweeetTweet),
                           #    'quotedTweet': tweet.quotedTweet,
                           'inReplyToTweetId': tweet.inReplyToTweetId,
                           #    'inReplyToUser': tweet.inReplyToUsers,
                           #    'mentionedUsers': tweet.mentionedUsers,
                           'coordinates': tweet.coordinates,
                           'place': tweet.place,
                           #    'hashtags': tweet.hastags,
                           'cashtags': tweet.cashtags,
                           #    'link': tweet.link,
                           #    'search': tweet.seacrh,
                           'likeCount': tweet.likeCount,
                           'retweetCount': tweet.retweetCount,
                           'lang': tweet.lang
                           })
        # j = json.dumps(tweets)
        return jsonify(tweets)
    except Exception as e:
        result = {
            "statusCode": 400,
            "error": e
        }
        return result
    
@app.post("/search")
def search():
    try:
        print(request.data)
        posts = json.loads(request.data)
        limit = posts['limit']
        keyword = posts['keyword']

        tweets = []

        scraper = twitterScrapper.TwitterSearchScraper(keyword)
        for i, tweet in enumerate(scraper.get_items()):
            print(tweet)
            if i > limit:
                break
            print(f"{i} content: {tweet}")
            tweets.append({"id": tweet.id,
                           "username": tweet.user.username,
                           'content': tweet.content,
                           'url': tweet.url,
                           'date': tweet.date,
                           'renderedContent': tweet.renderedContent,
                           'quoteCount': tweet.quoteCount,
                           'conversationId': tweet.conversationId,
                           'lang': tweet.lang,
                           'source': tweet.source,
                           'sourceUrl': tweet.sourceUrl,
                           'sourceLabel': tweet.sourceLabel,
                           #    'outlinks': jsonify(tweet.outLinks),
                           #    'tcooutlinks': tweet.tcooutLinks,
                           'media': tweet.media,
                           #    'retweetedTweet': json.dumps(tweet.retweeetTweet),
                           #    'quotedTweet': tweet.quotedTweet,
                           'inReplyToTweetId': tweet.inReplyToTweetId,
                           #    'inReplyToUser': tweet.inReplyToUsers,
                           #    'mentionedUsers': tweet.mentionedUsers,
                           'coordinates': tweet.coordinates,
                           'place': tweet.place,
                           #    'hashtags': tweet.hastags,
                           'cashtags': tweet.cashtags,
                           #    'link': tweet.link,
                           #    'search': tweet.seacrh,
                           'likeCount': tweet.likeCount,
                           'retweetCount': tweet.retweetCount,
                           'lang': tweet.lang
                           })
        return jsonify(tweets)
    except Exception as e:
        result = {
            "statusCode": 400,
            "error": e
        }
        return result
@app.post("/trend")
def trend():
    try:
        tweets = []

        scraper = twitterScrapper.TwitterTrendsScraper()
        for i, tweet in enumerate(scraper.get_items()):
            print(tweet)
            if i > 23:
                break
            print(f"{i} content: {tweet.name}")
            tweets.append({"name": tweet.name,
                           "domainContext": tweet.domainContext,
                           'totalTweets': tweet.metaDescription,
                           })

        j = json.dumps(tweets)
        return j
    except Exception as e:
        result = {
            "statusCode": 400,
            "error": e
        }
        return result

@app.post("/user")
def user():
    try:
        print(request.data)
        posts = json.loads(request.data)
        limit = posts['limit']
        keyword = posts['account']
        tweets = []

        scraper = twitterScrapper.TwitterUserScraper(keyword)
        for i, tweet in enumerate(scraper.get_items()):
            print(tweet)
            if i > limit:
                break
            print(f"{i} content: {tweet.content}")
            tweets.append({"id": tweet.id,
                           "username": tweet.user.username,
                           'content': tweet.content,
                           'url': tweet.url,
                           'date': tweet.date,
                           'renderedContent': tweet.renderedContent,
                           'replyCount': tweet.replyCount,
                           'retweetCount': tweet.retweetCount,
                           'likeCount': tweet.likeCount,
                           'quoteCount': tweet.quoteCount,
                           #    'conversationId': tweet.conversationId,
                           'source': tweet.source,
                           'sourceUrl': tweet.sourceUrl,
                           'sourceLabel': tweet.sourceLabel,
                           'sourceLabel': tweet.sourceLabel,
                           #    'outlinks': jsonify(tweet.outLinks),
                           #    'tcooutlinks': tweet.tcooutLinks,
                           'media': tweet.media,
                           #    'retweetedTweet': json.dumps(tweet.retweeetTweet),
                           #    'quotedTweet': tweet.quotedTweet,
                           'inReplyToTweetId': tweet.inReplyToTweetId,
                           #    'inReplyToUser': tweet.inReplyToUsers,
                           #    'mentionedUsers': tweet.mentionedUsers,
                           'coordinates': tweet.coordinates,
                           'place': tweet.place,
                           #    'hashtags': tweet.hastags,
                           'cashtags': tweet.cashtags,
                           #    'link': tweet.link,
                           #    'search': tweet.seacrh,
                           'likeCount': tweet.likeCount,
                           'retweetCount': tweet.retweetCount,
                           'lang': tweet.lang
                           })
        return jsonify(tweets)
    except Exception as e:
        result = {
            "statusCode": 400,
            "error": e
        }
        return result
    
if __name__ == "__main__":
    app.run(debug=True)
