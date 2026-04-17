import pandas as pd

def load_and_clean_data(path):

    df = pd.read_csv(path, encoding='latin1')

    # datetime fix
    df['InvoiceDate'] = pd.to_datetime(
        df['InvoiceDate'],
        errors='coerce'
    )

    df = df.dropna(subset=['InvoiceDate'])

    # time features
    df['Month'] = df['InvoiceDate'].dt.month
    df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek
    df['Hour'] = df['InvoiceDate'].dt.hour

    # clean invalid values
    df = df[df['UnitPrice'] > 0]
    df = df[df['Quantity'] > 0]

    return df
