# app.py
from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/distance')
def get_distance():
    try:
        with open("data3.txt", "r") as f:
            distance = int(f.read().strip())
        return jsonify({'distance': distance})
    except:
        return jsonify({'distance': -1})  # default if file missing or corrupt

if __name__ == '__main__':
    app.run(debug=True)
