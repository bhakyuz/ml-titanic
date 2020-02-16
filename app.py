from flask import Flask
from flask_restful import Resource, Api
from flask import request
import pandas as pd
import ml

app = Flask(__name__)
api = Api(app)

# Example 
# http://127.0.0.1:8000/?text=tata&toto=toktok&a=2

class Predict(Resource):
    def get(self):
        url_params = request.args
        df = pd.DataFrame.from_records(url_params, index=[0])
        df2 = ml.prepare_data(df, ml.REPLACEMENTS)
        return {'url_params': url_params, 'raw': df.to_dict(), 'preprocessed': df2.to_dict()}
        
api.add_resource(Predict, '/')

if __name__ == '__main__':
    app.run(debug=True)
