from flask import Flask , request
import pickle

import numpy as np

load_data = pickle.load(open('ml.pickle','rb'))

app = Flask(__name__)

@app.route('/model',methods=['POST'])

def hello_world():
    request_data  = request.get_json(force=True)
    sinangle = request_data['sinangle']
    cosangle = request_data['cosangle']
                           
    predict =  load_data.predict(np.array([[sinangle,cosangle]]))
    
    return "The prediction is {0}".format(predict)

if __name__ == "__main__":
    app.run(port=8000,debug=True)
    