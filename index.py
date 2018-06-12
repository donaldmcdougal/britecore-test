from flask import Flask, request, render_template, jsonify
import os.path
import sqlite3
from database import Client, ProductArea, FeatureRequest, DBSession

app = Flask(__name__)
session = DBSession()

@app.route("/")
def index():
    return "Hello World!"

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'test.html', name=name)

@app.route("/client")
def client():
    list = session.query(Client).all()
    return jsonify([e.to_json() for e in list])

@app.route('/product_area')
def product_area():
    list = session.query(ProductArea).all()
    return jsonify([e.to_json() for e in list])

@app.route('/feature_request')
def feature_request():
    list = session.query(FeatureRequest).all()
    return jsonify([e.to_json() for e in list])

if __name__ == "__main__":
    app.run()
