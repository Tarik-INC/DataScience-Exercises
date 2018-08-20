from flask import Flask, jsonify
import consumo_de_energia_KNN
app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome'


@app.route('/predict/oneday/<int:week_day>/', methods=['GET'])
def predict_one_day(week_day):
    if not(consumo_de_energia_KNN.model_trained):
        consumo_de_energia_KNN.train_model()

    resp = jsonify(consumo_de_energia_KNN.predict_one_day(week_day))
    resp.status_code = 200
    return resp


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
