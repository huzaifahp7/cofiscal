# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify, Response
import datetime
from flask_cors import CORS
import sys
import json
import numpy as np
import pickle
import joblib
import pandas as pd

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
myModel = pickle.load(open('LGBM_TRAINED_MODEL_2.pkl','rb'))
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/model', methods=['POST'])
def model():
	data = request.json
	prediction = myModel.predict([list(data.values())], num_iteration=myModel.best_iteration)
	return prediction.tolist()
    

# Route for seeing a data
@app.route('/hello')
def get_time():

	# Returning an api for showing in reactjs
	return {
		'Name':"geek", 
		"Age":"22",
		"Date":x, 
		"programming":"python"
		}


	
# Running app
if __name__ == '__main__':
	app.run(debug=True)




