from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def load_json_data():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception:
        return None

def load_csv_data():
    try:
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception:
        return None

def load_sqlite_data():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except Exception:
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source')
    item_id = request.args.get('id')
    data = []
    error = None

    if source == 'json':
        data = load_json_data()
    elif source == 'csv':
        data = load_csv_data()
    elif source == 'sql':
        data = load_sqlite_data()
    else:
        error = "Wrong source"

    if data is None:
        error = "Error reading data file or database"

    if not error and item_id:
        filtered = [item for item in data if str(item.get("id")) == str(item_id)]
        if filtered:
            data = filtered
        else:
            error = "Product not found"
            data = []

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
