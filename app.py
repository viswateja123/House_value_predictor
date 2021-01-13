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
        
            
            
        b = float(request.form['Old'])
        c = float(request.form['Dist'])
        d = int(request.form['No'])
        e = float(request.form['Long'])
        f = float(request.form['Lat'])
        
        temp_array = temp_array + [b,c,d,e,f]
        
        data = np.array([temp_array])
        my_prediction = (regressor.predict(data)[0])
              
        return render_template('result.html', x=my_prediction.round(3))



if __name__ == '__main__':
	app.run(debug=True)