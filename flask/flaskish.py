# initialize a simple flask application
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
from twitterConnect import get_tweets_with_username
#Set up Flask:
app = Flask(__name__)
#Set up Flask to bypass CORS:
cors = CORS(app)
#Create the receiver API POST endpoint:
@app.route("/receiver", methods=["POST"])
def postME():
    data = request.get_json()
    #  data = jsonify(data)
    data = data["twitter"]
    print(data)




    tweets = get_tweets_with_username(data["twitter"])
    tweets['stock'] = data["stock"]
    print(tweets)

    
    ################FOR TYLER#############################
    # # data has property stock and Alts  (data["stock"], data["Alts"])
    # # check if tweets have any of those words (those are the ones we will sentiment)
    # # if they do add a property called present to it
    # # use this to get you started

    # words = [data.stock] + data.Alts.split(" ")
    # for item in tweets.data:
    #     for word in words:
    #         if word in item.text:
    #             item.present = True
    #             break
    #         else:
    #             item.present = False
    # this might simply work already i didnt test it 
    ################FOR TYLER#############################
    


    #save the data to a file in a json structure
    with open('data.json', 'w') as outfile:
        json.dump(tweets, outfile)

    

    return jsonify(tweets)
    print(tweets)
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
