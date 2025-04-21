from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

def train_model():
    df = pd.read_csv('data/processed/analysis_ready.csv')

    X = df[['income', 'poverty_rate', 'income_poverty_ratio']]
    y = df['diagnosis_delay_days']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    joblib.dump(model, 'models/delay_predictor.pkl')

if __name__ == "__main__":
    train_model()
