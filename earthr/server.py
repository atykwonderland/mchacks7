from flask import Flask
import json
from db import col
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'hi'

@app.route('/foods',methods=['GET'])
def getAllFoods():
    data = col.find()
    response = []
    for data in documents:
        if (data["carbon-footprint_100g"] != ""):
            dic = dict()
            dic["product_name"]= str(data["product_name"])
            dic["generic_name"] = str(data["generic_name"])
            dic["quantity"] = str( data["quantity"])
            dic["serving_size"] = str(data["serving_size"])
            dic["packaging"] = str(data["packaging"])
            dic["carbon-footprint_100g"] = int(data["carbon-footprint_100g"])
            response.append(dic)
    return json.dumps(response)
    

if __name__ == '__main__':
    app.run(host=app.config['SERVER_NAME'], debug=True)
