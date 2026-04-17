from preprocessing import load_and_clean_data
from sklearn.linear_model import LinearRegression
import pickle

def train_model(df):

    df = df.copy()

    df['Price'] = df['UnitPrice']
    df['Demand'] = df['Quantity']

    # 🔥 encode product safely
    df['ProductCode'] = df['StockCode'].astype('category').cat.codes

    # INPUT FEATURES (NO STRUCTURE CHANGE IN PROJECT FLOW)
    X = df[['Price', 'Month', 'DayOfWeek', 'ProductCode']]
    y = df['Demand']

    model = LinearRegression()
    model.fit(X, y)

    pickle.dump(model, open('model.pkl', 'wb'))

    return model
