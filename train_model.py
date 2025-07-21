import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

# Sample expanded data (you should replace this with real data)
data = pd.DataFrame({
    'PM2.5': [30, 45, 60, 75, 90, 110, 130, 150, 170, 200],
    'NO2':   [10, 15, 25, 35, 45, 50, 60, 70, 80, 90],
    'SO2':   [2,  4,  6,  8,  10, 12, 14, 16, 18, 20],
    'CO':    [0.2, 0.3, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.4, 1.5],
    'O3':    [5, 10, 15, 18, 20, 23, 25, 28, 30, 35],
    'AQI':   [50, 70, 90, 110, 130, 150, 170, 190, 210, 250]
})

X = data[['PM2.5', 'NO2', 'SO2', 'CO', 'O3']]
y = data['AQI']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GradientBoostingRegressor()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Visualization
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

plt.figure()
plt.plot(y_test.values, label="Actual AQI", marker='o')
plt.plot(y_pred, label="Predicted AQI", marker='x')
plt.title("Actual vs Predicted AQI")
plt.xlabel("Sample Index")
plt.ylabel("AQI")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("✅ Model training complete. Saved as model.pkl.")
