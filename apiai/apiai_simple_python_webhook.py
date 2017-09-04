import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))
    res = "Hi, this is a sample web hook implementation"
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == '__main__':
	app.run(debug=True, port=5000, host='0.0.0.0')
