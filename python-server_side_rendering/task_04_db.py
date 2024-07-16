from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def read_csv(file_path):
    with open(file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        return list(csv_reader)


def read_sql():
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    data = cursor.fetchall()
    conn.close()
    return [
        dict(ix) for ix in data
    ]  # Convert sqlite3.Row objects to dictionaries


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    data = []
    error = None

    if source == "json":
        data = read_json("products.json")
    elif source == "csv":
        data = read_csv("products.csv")
    elif source == "sql":
        data = read_sql()
    else:
        error = "Wrong source"

    if product_id:
        data = [
            product for product in data if str(product.get("id")) == product_id
        ]
        if not data:
            error = "Product not found"

    return render_template("product_display.html", data=data, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
