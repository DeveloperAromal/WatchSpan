from flask import Flask, jsonify
from src.data.data import STORE_DATA
from src.tools.get_Inventory_data import get_inventory_data


app = Flask(__name__)

@app.route("/store", methods=["GET"])
def get_all_inventory_data():
    return jsonify(STORE_DATA)

@app.route("/", methods=["GET"])
def start():
    get_inventory_data()

    return jsonify({"status": "Active"})