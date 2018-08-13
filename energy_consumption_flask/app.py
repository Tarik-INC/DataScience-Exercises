from flask import Flask
import consumo_de_energia_KNN
app = Flask(__name__)


@app.route('/predict/oneday/<int:week_day>')
def predict_one_day(week_day):
    if consumo_de_energia_KNN.model_trained:
        return consumo_de_energia_KNN.predict_one_day(week_day)
    else:
        consumo_de_energia_KNN.train_model()
        print(consumo_de_energia_KNN.predict_one_day(week_day))
        return None

@app.route('/predict/week/')
def predict_week():
    if consumo_de_energia_KNN.model_trained:
        return consumo_de_energia_KNN.predict_week
    else:
        consumo_de_energia_KNN.train_model()
        return consumo_de_energia_KNN.predict_week()