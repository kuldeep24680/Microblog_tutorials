from app import app

@app.route('/')
def welcome():
	return "hi there!!"

@app.route('/index')
def index():
	return "Hello, World!"

@app.route('/finish')
def farewell():
	return "story is finish!!"
