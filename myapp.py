from flask import Flask, render_template, request, redirect, url_for, session, g, flash
import tweepy 

#############################################################################################
################################  TWEEPY SETUP  #################################################

consumer_key = 'KNY4Zvfpg3ZJw9HEXgYZgpEsV'
consumer_secret = 'omlOAjdQViBKm1IKVWQfa0xuPakw6qs8G3YgnVM796KuaEabVz'
access_token = '60773330-kwmBd0SRPws1b0xl9EqF6hqOGuzXp0gxU9dX1HKZi'
access_token_secret = 'Lxl9jZJIcS2QresKsaRaSEcxcCly5JVuA6gVBtrveY9Eh'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
##############################################################################################

app = Flask(__name__) 
 

# #---------------GETTING TWEETS SPECIFIC TO HASHTAG---------------
@app.route('/', methods=['GET', 'POST'])
def hash():
	return render_template('map.html')
# 	if request.method=='POST':
# 		hashtag = request.form['hashtag']
# 		h = tweepy.Cursor(api.search, q = hashtag, lang = "th").items()
# 		return render_template('hash.html', h = h, hashtag = hashtag)

# 	return render_template('map.html')


if (__name__ == "__main__"):
	app.debug = True
	app.run(threaded = True)
