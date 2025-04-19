import pandas as pd
import numpy as np

np.random.seed(42)
data = {
    'patient_id': np.arange(1, 501),
    'age': np.random.randint(18, 80, 500),
    'sex': np.random.choice(['M','F'], 500, p=[0.49,0.51]),
    'zip_code': np.random.choice(['60601','10001','90001','77001'], 500),
    'income': np.abs(np.random.normal(50000, 15000, 500)).astype(int),
    'education': np.random.choice(['HS','College','Grad'], 500, p=[0.4,0.4,0.2]),
    'diagnosis_delay_days': np.abs(np.random.normal(180, 90, 500)).astype(int)
}
pd.DataFrame(data).to_csv('data/raw/patients.csv', index=False)
print("Data generated successfully!")
