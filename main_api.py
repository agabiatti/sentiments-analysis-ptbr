from flask import Flask
from flask_restful import Resource, Api, reqparse
from joblib import load as load_joblib

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('message')

class Predict(Resource):
  def post(self):
    args = parser.parse_args()
    pipeline = load_joblib("models/sentiments.joblib")
    vector = pipeline.named_steps.vectorizer.transform([args['msg']])
    res = pipeline.named_steps.model.predict(vector)

    return { 'metadata': { 'model': 'Sentiments Analysis pt-BR', 'version': 1 }, 'predict': res[0] }, 200

api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')