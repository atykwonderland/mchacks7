from flask import Flask
import json
from db import col
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'hi', 200

@app.route('/foods',methods=['GET'])
def getAllFoods():
    data = col.find()
    response = []
    for d in data:
        if (d["carbon-footprint_100g"] != "" ):
            dic = dict()
            dic["product_name"]= str(d["product_name"])
            dic["generic_name"] = str(d["generic_name"])
            dic["quantity"] = str( d["quantity"])
            dic["serving_size"] = str(d["serving_size"])
            dic["packaging"] = str(d["packaging"])
            dic["carbon-footprint_100g"] = int(d["carbon-footprint_100g"])
            response.append(dic)
    return json.dumps(response).encode('utf-8'), 200
    

if __name__ == '__main__':
    app.run(host=app.config['SERVER_NAME'], debug=True)
