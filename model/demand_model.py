from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

def train_model(df):

    df = df.copy()

    # feature engineering
    df['Price'] = df['UnitPrice']
    df['Demand'] = df['Quantity']

    df['ProductCode'] = df['StockCode'].astype('category').cat.codes

    # INPUT FEATURES
    X = df[['Price', 'Month', 'DayOfWeek', 'ProductCode']]
    y = df['Demand']

    # split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # save model
    pickle.dump(model, open('model.pkl', 'wb'))

    return model
