from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user={'username':'kuldeep'}
	return render_template('index.html',title='Home',user=user)

@app.route('/index_posts')
def index_posts():
	user={'username':'kuldeep'}
	posts=[
		{
			'author':{'username':'kuldeep'},
			'body': 'You only live once!!'
		},
		{
			'author':{'username':'vicky'},
			'body': "I agree, but statiscally for 80 years, that's a hell lot of time!!"

		}
	]
	return render_template('index_posts.html',user=user,posts=posts)
