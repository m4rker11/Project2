import requests
# Create Twitter API function
# Pass in username string to query API for user ID then query again for tweets
def get_id(username):
    url = "https://api.twitter.com/2/users/by?usernames=" + username
    payload = {}
    headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANiRbAEAAAAAT0NxrtOvZEqLLnG5VdCSPFqPOCw%3Dm5Ktdnc7g7HGCv7cDWbYNjuHpTh0WzoyoWYJZdOqs1D487niHa'}
    id_response = requests.request("GET", url, headers = headers, data = payload).json()
    twitter_id = id_response['data'][0]['id'] 
    return twitter_id

# Create function to use twitter id to query for user tweets
def get_tweets(twitter_id):
    url = "https://api.twitter.com/2/users/" + twitter_id + "/tweets?max_results=100&tweet.fields=public_metrics"
    payload = {}
    headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANiRbAEAAAAAT0NxrtOvZEqLLnG5VdCSPFqPOCw%3Dm5Ktdnc7g7HGCv7cDWbYNjuHpTh0WzoyoWYJZdOqs1D487niHa'}
    tweets = requests.request("GET", url, headers = headers, data = payload).json()
    return tweets

def get_tweets_with_username(username):
    twitter_id = get_id(username)
    tweets = get_tweets(twitter_id)
    return tweets