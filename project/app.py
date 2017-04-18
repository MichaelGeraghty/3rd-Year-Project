#imports
from flask import Flask, render_template, request, redirect, url_for
from models import *

app = Flask(__name__)

#before request to initialise and connects the blog db before it is requested
@app.before_request
def before_request():
	initialise_db()

#wether it is succesful or fails connecting to the db it will close and displays exceptions if fails
@app.teardown_request
def teardown_request(exception):
	db.close()

#root dir with the date format to be rendered in home.html
@app.route('/')
def home():
#orders posts by latest .desc
	return render_template('home.html',posts=Post.select().order_by(Post.date.desc()))

#for creating a new post
@app.route('/new_post/')
def new_post():
	return render_template('new_post.html')
	
#about.html for information about site
@app.route('/about/')
def about():
	return render_template('about.html')

#To post into the database
#only allows a post method not accessable from users
@app.route('/create/', methods=['POST'])
def create_post():
	#creates the new post
	Post.create(
		title=request.form['title'],
		text=request.form['text'],
		content=request.form['content']
	)
	#allows the redirection back to home even if '/' is replaced ie will always redirect home
	return redirect(url_for('home'))


#running app using default port 5000
if __name__== '__main__':
	app.run(debug=True)
