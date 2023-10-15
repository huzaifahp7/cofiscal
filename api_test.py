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
from PaLM_script import *
import google.generativeai as palm
import re
import pytesseract
from pdf2image import convert_from_path
from pdfminer.high_level import extract_text
from ocr_revised import *

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

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
		if keys == 'debtToIncomeRatio' or keys == 'interestRate':
			data[keys] = float(data[keys])
		else:
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
		if file:
			if not os.path.exists(UPLOAD_FOLDER):
				os.makedirs(UPLOAD_FOLDER)
			filename = secure_filename(file.filename)
			file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			file.save(file_path)
		d['status'] = 1
		output = extract_features_from_pdf(file_path)
		print(output)
		ocr = {'Read':output}
	except Exception as e:
		print(f"Couldn't upload file {e}")
		d['status'] = 0
	
	json_object = json.dumps(ocr, indent=4)
	return json_object

@app.route('/gpt', methods=['POST'])
def analysis():
    data = request.json
    values = list(data.values())

    output = generate_text(
     str(values[1]),str(values[2]), str(values[3]), str(values[6]),str(values[7]),str(values[8]),int(values[-3]),str(values[-1])
)
    print(output)
    dicti = {
        'predict':output
        }
	
    json_object = json.dumps(dicti, indent=4)
    
    return json_object
    
	
# Running app
if __name__ == '__main__':
	app.run(debug=True)