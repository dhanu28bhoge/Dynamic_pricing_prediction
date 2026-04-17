import sys
import os
import json
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle

# =========================
# PATH SETUP
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "model"))
FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "frontend"))

sys.path.insert(0, MODEL_DIR)
from pricing_model import get_dynamic_price

# =========================
# FLASK INIT
# =========================
app = Flask(__name__, static_folder=FRONTEND_DIR)
CORS(app)

model = pickle.load(open('model.pkl', 'rb'))

DB_FILE = "db.json"

# =========================
# LOAD DATA
# =========================
if os.path.exists(DB_FILE):
    try:
        with open(DB_FILE, "r") as f:
            products_db = json.load(f)
    except:
        products_db = []
else:
    products_db = []

# =========================
# SAVE DATA
# =========================
def save_db():
    with open(DB_FILE, "w") as f:
        json.dump(products_db, f)

# =========================
# 🔥 BACKEND STATUS ROUTE (NEW)
# =========================
@app.route('/')
def serve_index():
    return send_from_directory(FRONTEND_DIR, 'homepage.html')

@app.route('/<path:filename>')
def serve_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)
# =========================
# DEMAND LOGIC (YOUR FINAL)
# =========================
def get_adjusted_demand(raw, price):
    raw = float(raw)
    raw = max(0, min(100, raw))

    # 🔥 FIXED SCALING
    normalized = raw / 2
    normalized = max(0, min(10, normalized))

    adjusted = normalized - (price / 100)

    return max(0, min(10, adjusted))

def get_demand_label(adjusted):
    if adjusted >= 6:
        return "High Demand"
    elif adjusted >= 3:
        return "Moderate Demand"
    else:
        return "Low Demand"

# =========================
# ADD PRODUCT
# =========================
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json

    price = float(data["price"])
    month = int(data["month"])

    raw_demand = model.predict([[
        price,
        month,
        int(data["day"]),
        int(data["product_code"])
    ]])[0]

    adjusted = get_adjusted_demand(raw_demand, price)

    product = {
        "name": data["name"],
        "price": price,
        "demand": round(adjusted, 2),
        "demand_level": get_demand_label(adjusted),
        "suggested_price": round(get_dynamic_price(adjusted, price, month), 2)
    }

    products_db.append(product)
    save_db()

    return jsonify({
    "name": product["name"],
    "predicted_demand": product["demand"],
    "label": product["demand_level"],
    "price": product["suggested_price"]
})
# =========================
# ANALYTICS DATA
# =========================
@app.route('/analytics_data')
def analytics_data():
    return jsonify(products_db)

# =========================
# PREDICT API
# =========================
@app.route('/predict')
def predict():
    price = float(request.args.get('price'))
    month = int(request.args.get('month'))
    day = int(request.args.get('day'))
    code = int(request.args.get('product_code'))

    raw = model.predict([[price, month, day, code]])[0]
    adjusted = get_adjusted_demand(raw, price)

    return jsonify({
        "predicted_demand": float(adjusted),
        "label": get_demand_label(adjusted),
        "price": round(get_dynamic_price(adjusted, price, month), 2)
    })

# =========================
# RUN SERVER
# =========================
if __name__ == '__main__':
    print("🚀 Starting AI Pricing Backend...")
    app.run(debug=True, use_reloader=False)
