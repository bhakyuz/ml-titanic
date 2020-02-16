from flask import Flask
from flask_restful import Resource, Api
from flask import request
import pandas as pd


app = Flask(__name__)
api = Api(app)

# Example 
# http://127.0.0.1:8000/?text=tata&toto=toktok&a=2

class HelloWorld(Resource):
    def get(self):
        url_params = request.args
        df = pd.DataFrame.from_records(url_params, index=[0])
        return {'url_params': url_params, 'df': df.to_dict()}
        
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)