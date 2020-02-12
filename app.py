from flask import Flask, jsonify, g

from resources.kids import kids 
import models 

DEBUG = True 
PORT = 8000

app = Flask(__name__) 

app.register_blueprint(kids, url_prefix='/api/v1/kids')

@app.before_request 
def before_request():

  g.db = models.DATABASE
  g.db.connect()


@app.after_request 
def after_request(response):
  g.db.close()
  return response 

@app.route('/')  
def index():
  return 'Hello, world!'

@app.route('/say_hello/<username>')
def say_hello(username): 
  return "Hello {}".format(username)

if __name__ == '__main__':
  models.initialize() 
  app.run(debug=DEBUG, port=PORT)  
