# required packages 
from flask import Flask,render_template,request,make_response,jsonify
from helper import Helper

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/output/',methods=["POST",'GET'])
def output():
    bs64string = request.get_json()
    result = Helper().predict(bs64string)
    if(result['acc'] > 60):
        res = make_response(jsonify(result),200)
        return res
    
    result['cls'] = 'Low Accuracy'
    res = make_response(jsonify(result),200)
    return res
    
    


if __name__ == '__main__':
    app.run(debug=True)
















