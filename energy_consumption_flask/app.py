from flask import Flask, jsonify, json, request
import consumo_de_energia_KNN
app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome'


@app.route('/predict/oneday/', methods=['POST'])
def predict_one_day(week_day):
    if not(consumo_de_energia_KNN.model_trained):
        consumo_de_energia_KNN.train_model()

    if request.headers['Content-Type'] == 'application/json':
        int_request_data = int(request.json['day'])
        resp = jsonify(consumo_de_energia_KNN.predict_one_day(int_request_data))
        resp.status_code = 200
        return resp
    else:
        return None


@app.route('/predict/week/', methods=['GET'])
def predict_week():
    if not(consumo_de_energia_KNN.model_trained):
        consumo_de_energia_KNN.train_model()

    resp = jsonify(consumo_de_energia_KNN.predict_week())
    resp.status_code = 200
    print(resp)
    return resp


if __name__ == 'main':
    app.run(debug=True)
