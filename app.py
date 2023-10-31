from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Essa é minha primeira aplicação em Flask!'

app.run(host='0.0.0.0', port=1026)