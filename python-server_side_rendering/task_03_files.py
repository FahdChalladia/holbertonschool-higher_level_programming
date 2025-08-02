from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_json_data(filename='products.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        return []

def load_csv_data(filename='products.csv'):
    data = []
    try:
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Ensure proper type conversion
                data.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except Exception as e:
        pass
    return data

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    # Load data based on source
    if source == 'json':
        products = load_json_data()
    elif source == 'csv':
        products = load_csv_data()
    else:
        error = 'Wrong source'
        return render_template('product_display.html', error=error)

    # Filter by ID if provided
    if product_id is not None:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            error = 'Product not found'

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)
