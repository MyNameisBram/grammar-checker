from flask import Flask, jsonify, request
from utilities import predict_func


app = Flask(__name__)


@app.post('/predict')
def predict():
    
    data = request.json
    
    try:
        sample = data['orig_text', 'suggested_text']
    except KeyError:
        return jsonify({'error': 'No text sent'})

    #sample = [sample]
    predictions = predict_func(sample)

    try:
        result = jsonify(predictions[0])
       
    except TypeError as e:
        result = jsonify({'error': str(e)})
    return result
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
