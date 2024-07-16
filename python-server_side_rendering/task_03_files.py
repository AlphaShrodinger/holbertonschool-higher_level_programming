from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def read_csv(file_path):
    with open(file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        return list(csv_reader)


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
    else:
        error = "Wrong source"

    if product_id:
        data = [
            product for product in data if str(product.get("id")) == product_id
        ]
        if not data:
            error = "Product not found"

    return render_template("product_display.html", data=data, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
