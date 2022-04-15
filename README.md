# Using Twitter Sentiment Analysis of Key Individuals to Predict Stock Prices

The purpose of this project is to create an application that performs a sentiment analysis of specific Twitter user tweets to determine if those tweets had any effect on a stock price increasing or decreasing. The front end of the application is a webpage that allows a user to input a Twitter handle and a stock/cryptocurrency. Once submitted, the current pricing trends are shown through Tradingview and the back end of the application retrieves the Twitter ID number of the username that was entered to return tweets from that user. From there, the tweets are run through a sentiment analysis model to ultimately determine if the tweet sentiments had any influence on the prices of the stocks that were tweeted about. 

---

## Technologies Used

The front end of the application is coded in Javascript. The backend and machine learning portions of the application are coded in Python. Flask was used to communicate between the front and back ends. The machine learning algorithms emphasized the scikit-learn library to run Logistic Regression, Decision Tree Classifier, and Random Forest Classifier. 
  
---

## Usage
The webpage allows a user to input a Twitter handle, stock or cryptocurrency of their choice from Tradingview, and any other keywords. Once submitted, the app queries the Twitter API to return the tweets of the handle that was entered. These tweets are run through the machine learning algorithms on the back end and ultimately display in the webpage along with a table that shows the number of likes and retweets, whether or not the keywords were mentioned in the tweet, the timestamp of the tweet, and a sentiment score based on the results of the sentiment analysis. The screenshot below shows the results of a query:

![app](https://raw.githubusercontent.com/m4rker11/Project2/main/p2app.png)

The second great feature of the webpage is an interactive widget from TradingView that allows the user to display the simple moving average for the stock or cryptocurreny that they chose. By scrolling through the returned tweets and analyzing whether or not the tweet had any sentiment score or if the keywords entered were present in the tweet, the user can simply check the timestamp of the tweet and then use the TradingView chart to the right to physically maneuver to that specific date and time to see how the price of the stock was effected in the aftermath of the tweet being posted. The following shows the webpage with TradingView enabled on the right side of the screen:

![doge](https://github.com/m4rker11/Project2/blob/main/doge.png)

---

## Contributors

Project 2 Team 6 Group Members are Mark Zarutin, Jerry Ross, Jay Sen, and Tyler Castleberry.

---

## License

MIT License

Copyright (c) 2022

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.