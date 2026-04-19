# Dynamic Pricing with ML

> **For the full styled version, open [`README_Dynamic_Pricing.html`](./README_Dynamic_Pricing.html) in a browser.**

---

## Author
**Dhanashree Tukaram Bhoge**
Dynamic Pricing with ML · DSBDA Project

---

## Badges
`Python 3.10+` · `Scikit-learn` · `Random Forest` · `Pandas · NumPy` · `Jupyter Notebook`

---

## Overview

This notebook trains a machine learning model on the **Online Retail II dataset** to predict how many units a product will sell (demand) given its price, timing, and product attributes. By modelling demand as a function of `UnitPrice`, this creates the foundation for a dynamic pricing engine — raise the price when demand is inelastic, lower it to move inventory.

| Stat | Value |
|------|-------|
| R² | Score metric |
| Trees in forest | 300 |
| Train / test split | 80 / 20 |
| Input features | 6 |

---

## What This Project Does

| Component | Detail |
|-----------|--------|
| **Dataset** | Online Retail II — multi-country transaction records with invoice date, stock codes, unit prices, quantities, and customer IDs |
| **Model** | Random Forest Regressor with 300 estimators, max depth 15 |
| **Target variable** | `Quantity` — units sold per transaction line, proxy for demand elasticity |
| **Evaluation** | R² score, MAE, scatter plot of actual vs predicted demand |

---

## End-to-End Pipeline

```
Load CSV  →  Clean Data  →  Feature Engineering  →  Encode  →  Train/Test Split
                                                                       ↓
Visualise  ←  Evaluate  ←  Predict  ←  Train Random Forest  ←────────┘
```

**Stages:**
1. **Load CSV** — `online_retail_II.csv`, ISO-8859-1 encoding
2. **Clean data** — drop nulls, filter `Quantity > 0` and `UnitPrice > 0`
3. **Feature engineering** — extract `Month`, `Day`, `DayOfWeek` from `InvoiceDate`
4. **Encode** — `LabelEncoder` on `StockCode` and `Country`
5. **Train/test split** — 80% train, 20% test, `random_state=42`
6. **Train Random Forest** — `n_estimators=300`, `max_depth=15`, `n_jobs=-1`
7. **Predict** — `rf_model.predict(X_test)`
8. **Evaluate** — R² score, MAE
9. **Visualise** — actual vs predicted scatter plot

---

## Input Features → Target

| Feature | Source Column | Type | Note |
|---------|--------------|------|------|
| `UnitPrice` | UnitPrice | numeric | Core pricing signal |
| `Month` | InvoiceDate | derived | Seasonal demand patterns |
| `Day` | InvoiceDate | derived | Within-month fluctuation |
| `DayOfWeek` | InvoiceDate | derived | Weekday vs weekend behaviour |
| `StockCode_encoded` | StockCode | encoded | Product identity |
| `Country_encoded` | Country | encoded | Geographic market |

**Target:** `Quantity` (units sold per transaction)

> **Why no feature scaling?** Random Forest is tree-based — it splits on thresholds, not distances. Scaling has zero effect and is intentionally omitted.

---

## Model Configuration

```python
from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(
    n_estimators=300,     # 300 decision trees — more stable, slower
    max_depth=15,         # caps tree growth to prevent overfitting
    min_samples_split=5,  # min samples needed to split a node
    min_samples_leaf=2,   # min samples in each leaf node
    random_state=42,      # reproducible results
    n_jobs=-1             # use all CPU cores for parallel training
)
```

---

## Tech Stack

| Layer | Libraries |
|-------|-----------|
| Data | pandas, numpy, matplotlib |
| ML | scikit-learn, RandomForestRegressor, LabelEncoder |
| Environment | Python 3.10+, Jupyter Notebook, Anaconda / pip |

---

## How to Run

**1. Clone the repository**
```bash
git clone <your-repo-url>
cd dynamic_pricing
```

**2. Install dependencies**
```bash
# via pip
pip install pandas numpy matplotlib scikit-learn jupyter

# or via conda
conda install pandas numpy matplotlib scikit-learn jupyter
```

**3. Download the dataset**

Get **Online Retail II** from the [UCI ML Repository](https://archive.ics.uci.edu/dataset/502/online+retail+ii) and place it at:
```
dataset/online_retail_II.csv
```

> ⚠️ **Path note:** Cell 2 has a hardcoded Windows path (`C:\Users\dhanashree bhoge\Downloads\...`). Update it to your own local path before running.

**4. Open the notebook**
```bash
jupyter notebook accuracy/Dsbda.ipynb
```

**5. Run all cells**

Select **Kernel → Restart & Run All**. The final cells output R², MAE, and a scatter plot.

---

## Expected Output

```
R2 Score:     0.XXXX
Accuracy (%): XX.XX
MAE:          X.XXXX
```

- **R² Score** — proportion of variance explained (1.0 = perfect). Typically 0.40–0.75 for this dataset.
- **Accuracy (%)** — R² × 100
- **MAE** — mean absolute error in units of `Quantity`. Lower is better.
- **Scatter plot** — "Actual Demand vs Predicted Demand". Points along the diagonal = good fit.

> **Interpreting R²:** Because `Quantity` is inherently noisy, an R² of 0.50–0.65 is a solid result. The model captures systematic price-demand relationships while acknowledging irreducible noise.

---

## How This Enables Dynamic Pricing

The trained model maps `(price, product, market, timing)` → `predicted demand`. A pricing engine can simulate revenue at different price points:

```python
# Pseudo-code: revenue optimisation loop
best_price, best_revenue = 0, 0

for price in linspace(min_price, max_price, steps=100):
    features = [price, month, day, dow, stock_enc, country_enc]
    predicted_qty = rf_model.predict([features])[0]
    revenue = price * predicted_qty

    if revenue > best_revenue:
        best_price, best_revenue = price, revenue

print(f"Optimal price: £{best_price:.2f} → predicted revenue: £{best_revenue:.2f}")
```

**Use cases:**
- **Peak season pricing** — Month and DayOfWeek features let the model charge more during high-demand periods
- **Market segmentation** — Country encoding allows different optimal prices per geographic market
- **Inventory clearance** — Find the lowest price that still maximises revenue × margin
- **Real-time updates** — Retrain weekly on new transaction data

---

## Project Structure

```
dynamic_pricing/
│
├── accuracy/
│   └── Dsbda.ipynb               # Main notebook — data → model → evaluation
│
├── dataset/                      # (create this folder)
│   └── online_retail_II.csv      # UCI dataset — not included in repo
│
├── README.md                     # This file (plain text)
└── README_Dynamic_Pricing.html   # Full styled version (open in browser)
```

---

## Possible Improvements

- Add **price elasticity coefficient** as a derived feature (% Δ demand / % Δ price per product)
- Try **XGBoost or LightGBM** for faster training and potentially better accuracy
- Add **cross-validation** (k-fold) instead of a single train/test split
- Include **competitor pricing** data to model relative price effects
- Build a **Streamlit dashboard** to expose the model as an interactive pricing tool
- Use **SHAP values** to explain which features drive demand predictions
- Handle **target variable skew** — `Quantity` is right-skewed; a log transform may improve R²

---

## License

MIT License

---

*Built with Python · scikit-learn · Jupyter*
*Dataset: [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii)*
