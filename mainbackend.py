import os
import pymongo
import json
import random

import hashlib
import time
from flask import jsonify

from hashlib import sha256
import redis





def hashcalc(st):


    hash_object = hashlib.md5(st.encode())
    h = str(hash_object.hexdigest())
    return h



def initsystem():

    redisurl = os.environ.get('REDISURL')
    redisport = os.environ.get('REDISPORT')
    redispw = os.environ.get('REDISPW')

    r = redis.Redis(host=redisurl, port=redisport, password=redispw)



    

    return r






def dummy(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    if request.method == 'OPTIONS':
        # Allows GET requests from origin https://mydomain.com with
        # Authorization header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Max-Age': '3600',
            'Access-Control-Allow-Credentials': 'true'
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    }

    request_json = request.get_json()

    db = initsystem()
    
    if request.method == 'GET':
      msg = db.get('sahaywelcome')
      msg = msg.decode()

      return msg



    retjson = {}

    action = request_json['action']

    if action == "getmeds":
        
        meds = r.get('meds')
      
        return json.dumps({"length": len(meds),
                        "meds": meds})
    if action == "getplasma":
        
        plasma = r.get('plasma')
      
        return json.dumps({"length": len(plasma),
                        "meds": plasma})
    if action == "getblood":
        
        blood = r.get('blood')
      
        return json.dumps({"length": len(blood),
                        "meds": blood})


    retstr = "action not done"

    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return retstr
