from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def f0():
	return jsonify(res="Hello World")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
