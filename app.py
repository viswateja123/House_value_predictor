# Importing essential libraries

# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'abc.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
            
            
            
        overs = float(request.form['Old'])
        runs = float(request.form['Dist'])
        wickets = float(request.form['No'])
        runs_in_prev_5 = float(request.form['Long'])
        wickets_in_prev_5 = float(request.form['Lat'])
        
        temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        
        data = np.array([temp_array])
        my_prediction = float(regressor.predict(data)[0])
              
        return render_template('result.html',r=my_prediction)



if __name__ == '__main__':
	app.run(debug=True)	