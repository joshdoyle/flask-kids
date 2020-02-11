from flask import Flask, jsonify

DEBUG = True
PORT = 8000

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, kids!'

@app.route('/say_hello/<username>')
def say_hello(username): # this func takes URL param as arg
  return "Hello {}".format(username)	

if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)