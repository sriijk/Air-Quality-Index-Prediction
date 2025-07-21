# 🌫️ AQI Prediction Web App using Machine Learning

This project predicts the **Air Quality Index (AQI)** using pollutant levels like **PM2.5, NO₂, SO₂, CO, and O₃**, through a machine learning model. Built with **Streamlit**, it offers an interactive web interface for both individual and bulk predictions.

<p align="center">
  <img src="https://atovio.in/cdn/shop/articles/Air_Quality_Level.jpg?v=1744094358" width="500" alt= "Air Qality Index"/>
</p>


---

## 📌 Features

- 🧪 **Real-time AQI Prediction** – Enter pollutant values manually
- 📂 **Bulk Prediction** – Upload CSV files and get AQI predictions for each row
- 📊 **Visualizations** – Feature correlation heatmap and actual vs predicted AQI graphs
- 🌍 **Multi-page UI** – Home, About, Prediction, Services, and Contact
- 💾 **Model Trained** – Using Gradient Boosting Regressor (via scikit-learn)

---

## 🧠 Technologies Used

| Category       | Tools / Libraries                        |
|----------------|-------------------------------------------|
| ML Model       | `GradientBoostingRegressor` (sklearn)    |
| Language       | Python                                   |
| Frontend       | Streamlit                                |
| Data Handling  | pandas, numpy                            |
| Visualization  | seaborn, matplotlib                      |
| Model Saving   | pickle                                   |

---

## 📈 Sample Visualizations

### 🔥 Correlation Heatmap
 <img src="correlation_heatmap.png" width="500" alt= "Heatmap"/>

### 📉 Actual vs Predicted AQI
 <img src="actual_vs_predicted.png" width="500" alt= "Actual vs Predicted AQI Graph"/>

---

## 🚀 Live Demo

🌐 Hosted on **Streamlit Cloud**:  
[🔗 Click Here to Try the App]([https://your-app-link.streamlit.app](https://air-quality-index-prediction-9ow6uwsmb3arig5kmkrrbb.streamlit.app/))  

---

## 📦 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/aqi-predictor.git
cd aqi-predictor

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlit_app.py

```
---

📁 File Structure

```
aqi-predictor/
├── aqi_predictor.py       # Loads model and makes predictions
├── streamlit_app.py       # Main Streamlit UI
├── train_model.py         # (Optional) Model training script
├── model.pkl              # Trained Gradient Boosting model
├── api_test_data.csv      # Sample input data (CSV)
├── Template images 
|   ├── Figure 1
|   ├── Figure 2
|   └── Figure 3  
├── correlation_heatmap.png
├── actual_vs_predicted.png
└── requirements.txt       # Python dependencies

```
---

## 🔭 Future Scope

- 🌐 Integrate real-time AQI data using government APIs (like CPCB)
- 📍 Add geolocation-based AQI prediction
- 📱 Build a mobile version (Android/iOS)
- ❤️ Add health advisory messages based on AQI category
- 📊 Include interactive trend visualizations across cities

---

## Developed By:

Srishti Bhatnagar
