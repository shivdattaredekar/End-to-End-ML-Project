from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

app = Flask(__name__)

# Load pickle file
# Open the file in read-binary mode
with open('regmodel.pkl', 'rb') as file:
    # Load the pickled object
    regmodel = pickle.load(file)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data) # it is in a dictionary format
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])




if __name__ == "__main__":
    app.run(debug=True, port= 5001)
