# initialize a simple flask application
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

#Set up Flask:
app = Flask(__name__)
#Set up Flask to bypass CORS:
cors = CORS(app)
#Create the receiver API POST endpoint:
@app.route("/receiver", methods=["POST"])
def postME():
 data = request.get_json()
#  data = jsonify(data)
 print(data)
 return data

# Create Twitter API function
# Pass in username string to query API for user ID then query again for tweets
def get_id(username):
    url = "https://api.twitter.com/2/users/by?usernames=" + username
    payload = {}
    headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANiRbAEAAAAAT0NxrtOvZEqLLnG5VdCSPFqPOCw%3Dm5Ktdnc7g7HGCv7cDWbYNjuHpTh0WzoyoWYJZdOqs1D487niHa',
    'Cookie': 'guest_id=v1%3A164940024030665997'
    }
    id_response = requests.request("GET", url, headers = headers, data = payload).json()
    twitter_id = id_response['data'][0]['id'] 
    return twitter_id

# Create function to use twitter id to query for user tweets
def get_tweets(twitter_id):
    url = "https://api.twitter.com/2/users/" + twitter_id + "/tweets?max_results=100&tweet.fields=public_metrics"
    payload = {}
    headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANiRbAEAAAAAT0NxrtOvZEqLLnG5VdCSPFqPOCw%3Dm5Ktdnc7g7HGCv7cDWbYNjuHpTh0WzoyoWYJZdOqs1D487niHa',
    'Cookie': 'guest_id=v1%3A164940024030665997'
    }
    tweets = requests.request("GET", url, headers = headers, data = payload).json()
    return tweets


if __name__ == "__main__": 
 app.run(debug=True)
