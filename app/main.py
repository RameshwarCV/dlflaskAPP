from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/predict',methods=["POST"])
def predict():

    return jsonify({'results':1})
