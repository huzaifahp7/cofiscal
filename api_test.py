# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify, Response, session
import datetime
from flask_cors import CORS
import sys
import json
import numpy as np
import pickle
import joblib
import pandas as pd
from neighbours import *
import os
import logging
from werkzeug.utils import secure_filename
from io import BytesIO

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

x = datetime.datetime.now()
UPLOAD_FOLDER = '/'

# Initializing flask app
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
myModel = pickle.load(open('LGBM_TRAINED_MODEL_2.pkl','rb'))
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/model', methods=['POST'])
def model():
	data = request.json
	prediction = myModel.predict([list(data.values())], num_iteration=myModel.best_iteration)
	print(f"Debugger: {prediction.tolist()}")
	for keys in data:
		data[keys] = int(data[keys])
	nodeNeighbour = neigh(list(data.values()))

	mList = [nodeNeighbour.iloc[:1,:].values.flatten().tolist(),
		  nodeNeighbour.iloc[1:2,:].values.flatten().tolist(),
		  nodeNeighbour.iloc[2:3,:].values.flatten().tolist(),
		  nodeNeighbour.iloc[3:4,:].values.flatten().tolist(),
		  nodeNeighbour.iloc[4:5,:].values.flatten().tolist(),
		  nodeNeighbour.iloc[5:6,:].values.flatten().tolist(),
		  nodeNeighbour.iloc[6:,:].values.flatten().tolist()
		  ]
	
	# combining all lists into json
	dict = {
		'prediction':prediction.tolist()[0],
		'neighbour':mList
    }
	json_object = json.dumps(dict, indent=4)
	return json_object
    

@app.route('/upload', methods=['POST'])
def upload():
	"""Handles the upload of a file."""
	d = dict()
	try:
		file = request.files['file_from_react']
		filename = file.filename
		print(f"Uploading file {filename}")
		file_bytes = file.read()
		file_content = BytesIO(file_bytes).readlines()
		print(file_content)
		d['status'] = 1
	
	except Exception as e:
		print(f"Couldn't upload file {e}")
		d['status'] = 0

	return jsonify(d)

	
# Running app
if __name__ == '__main__':
	app.run(debug=True)

# flask_cors.CORS(app, expose_headers='Authorization')


