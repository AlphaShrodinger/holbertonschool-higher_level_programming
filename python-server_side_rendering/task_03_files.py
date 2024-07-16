from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to the Flask App'


@app.route('/product_display')
def product_display():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        error_message = 'Wrong source parameter. Use "json" or "csv".'
        return render_template('product_display.html', error_message=error_message)

    if source == 'json':
        products_data = read_json_data('products.json')
    elif source == 'csv':
        products_data = read_csv_data('products.csv')

    if product_id:
        filtered_products = [
            product for product in products_data if product['id'] == product_id]
        if not filtered_products:
            error_message = f'Product not found with ID: {product_id}'
            return render_template('product_display.html', error_message=error_message)

        products_data = filtered_products

    return render_template('product_display.html', products=products_data)


def read_json_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def read_csv_data(filename):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data


if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)
