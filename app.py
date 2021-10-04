from flask import Flask, render_template, request
import tweepy 
# import pyodbc 
import pandas as pd

#############################################################################################
################################  DB SETUP  #################################################

server = '192.168.75.126' 
database = 'DB_OpenData' 
username = 'sa' 
password = 'Bj4free' 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# conn = pyodbc.connect('DRIVER={FreeTDS};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password+';TDS_VERSION=7.2')
cursor = conn.cursor()



#############################################################################################
################################  TWEEPY SETUP  #############################################

consumer_key = 'KNY4Zvfpg3ZJw9HEXgYZgpEsV'
consumer_secret = 'omlOAjdQViBKm1IKVWQfa0xuPakw6qs8G3YgnVM796KuaEabVz'
access_token = '60773330-kwmBd0SRPws1b0xl9EqF6hqOGuzXp0gxU9dX1HKZi'
access_token_secret = 'Lxl9jZJIcS2QresKsaRaSEcxcCly5JVuA6gVBtrveY9Eh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

##############################################################################################

app = Flask(__name__) 

#---------------GETTING TWEETS SPECIFIC TO HASHTAG---------------
@app.route('/', methods=['GET', 'POST'])
def hash():
	if request.method=='POST':
		hashtag = request.form['hashtag']
		h = tweepy.Cursor(api.search_tweets, q = hashtag, lang = "th").items()
		data_tweet = tweepy.Cursor(api.search_tweets, q = hashtag, lang = "th").items()

		users_locs = [[ tweet.created_at, tweet.text, tweet.user.followers_count,tweet.retweet_count, tweet.favorite_count] for tweet in data_tweet]

		tweet_df = pd.DataFrame(data=users_locs, columns=['time_stamp', 'text', 'followers_count', 'retweet_count','favorite_count'])
		
		for index, row in tweet_df.iterrows():
			cursor.execute("INSERT INTO dbo.data_tweet (date_time,tweet_text,retweet) values(?,?,?)", row.time_stamp, row.text, row.retweet_count)
			conn.commit()

		cursor.close()
		return render_template('hash.html', h = h, hashtag = hashtag)

	return render_template('map.html')

#---------------GETTING TWEETS SCHEDULER---------------

if (__name__ == "__main__"):

	app.debug = True
	app.run(threaded = True)
