
import models
from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

kids = Blueprint('kids', 'kids')

@kids.route('/', methods=['GET'])
def kids_index():
  return "kids resource working"

@kids.route('/', methods=['POST'])
def create_kid():
  payload = request.get_json() 
  print(payload) 


  kid = models.Kid.create(name=payload['name'], age=payload['age'], gender=payload['gender'])

  print(kid) 
  print(kid.__dict__) 
  print(dir(kid)) 

  kid_dict=model_to_dict(kid)

  return jsonify(data=kid_dict, status={'message': 'Successfully created kid!'}), 201