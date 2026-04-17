from preprocessing import load_and_clean_data
from demand_model import train_model

# load dataset (UCI Online Retail II)
df = load_and_clean_data(
    r'C:\Users\dhanashree bhoge\Downloads\DSBDA\dataset\online_retail_II.csv'
)

# train model
model = train_model(df)

print("✅ Model trained successfully!")
