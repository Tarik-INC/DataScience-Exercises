from flask import Flask, jsonify, request
import consumo_de_energia_KNN
app = Flask(__name__)


@app.errorhandler(400)
def invalid_json(error=None):
    message = {
        'status': 400,
        'message': 'Bad Request: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp


@app.route('/')
def api_root():
    return 'Welcome'


@app.route('/train/', methods=['GET', 'POST'])
def train():
    if(request.method == 'GET'):
        consumo_de_energia_KNN.train_model()

    elif(request.method == 'POST' and request.headers['Content-Type'] == 'application/json'):
        data_post = request.json
        consumo_de_energia_KNN.train_model(neighbors=data_post['neighbors'])


@app.route('/predict/oneday/', methods=['POST'])
def predict_one_day(week_day):

    if request.headers['Content-Type'] == 'application/json':
        
        try:
            int_request_data = int(request.json['day'])
        except KeyError :
            invalid_json()
       
        resp = jsonify(
            consumo_de_energia_KNN.predict_one_day(int_request_data))
        
        resp.status_code = 200
        return resp
    else:
         invalid_json()


@app.route('/predict/week/', methods=['GET'])
def predict_week():

    resp = jsonify(consumo_de_energia_KNN.predict_week())
    resp.status_code = 200
    return resp



if __name__ == '__main__':
    app.run(debug=True)
