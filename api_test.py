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
from neighbours import *

x = datetime.datetime.now()

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

@app.route('/upload', methods=['POST'])
def fileUpload():
    target=os.path.join(UPLOAD_FOLDER,'test_docs')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    file = request.files['file'] 
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    session['uploadFilePath']=destination
    return destination

	
# Running app
if __name__ == '__main__':
	app.run(debug=True)




