from flask import Flask, jsonify
from src.data.data import STORE_DATA

app = Flask(__name__)

@app.route("/store", methods=["GET"])
def get_all_inventory_data():
    return jsonify(STORE_DATA)
