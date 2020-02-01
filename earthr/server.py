from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'hi'

if __name__ == '__main__':
    app.run(host=app.config['SERVER_NAME'], debug=True)
