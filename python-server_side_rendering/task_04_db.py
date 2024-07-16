from flask import Flask, render_template, request, json
import csv
import sqlite3

app = Flask(__name__)


def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def read_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data


def read_sqlite(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    data = [{'id': row[0], 'name': row[1],
             'category': row[2], 'price': row[3]} for row in rows]
    return data


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    elif source == 'sql':
        products = read_sqlite('products.db')
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        products = [product for product in products if str(
            product['id']) == str(product_id)]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
