import streamlit as st
import pandas as pd
from aqi_predictor import predict_aqi

st.set_page_config(page_title="AQI Dashboard", layout="wide")

# Set default page in session state
if "page" not in st.session_state:
    st.session_state.page = "home"

# --- Sidebar Navigation ---
st.sidebar.title("🌍 AQI Dashboard")
if st.sidebar.button("🏠 Home"):
    st.session_state.page = "home"
if st.sidebar.button("ℹ️ About"):
    st.session_state.page = "about"
if st.sidebar.button("🔮 Prediction"):
    st.session_state.page = "prediction"
if st.sidebar.button("🛠️ Services"):
    st.session_state.page = "services"
if st.sidebar.button("📬 Contact"):
    st.session_state.page = "contact"

# --- Page Routing ---
page = st.session_state.page

if page == "home":
    st.title("🌍 Welcome to the AQI Prediction App")
    st.markdown("""
    ---
    🌫️ **Track. Predict. Understand.**  
    This intelligent dashboard helps you estimate the **Air Quality Index (AQI)** based on five major pollutants:
    - PM2.5 (fine particulate matter)
    - NO₂ (Nitrogen Dioxide)
    - SO₂ (Sulfur Dioxide)
    - CO (Carbon Monoxide)
    - O₃ (Ozone)
            ---
                """)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://atovio.in/cdn/shop/articles/Air_Quality_Level.jpg?v=1744094358",width=450)


    st.markdown("""
                ---
    🔬 Powered by machine learning, our model not only predicts AQI but also helps interpret how safe or harmful the air around you might be — useful for **students**, **health professionals**, **urban planners**, and **environmental researchers**.

    📁 You can predict:
    - Individual AQI from manual input.
    - Multiple values at once using a CSV upload.
    
    ---
    🔗 **Explore More:**
    - Navigate to **Prediction** to try it out.
    - Visit **About** to understand the tech behind it.
    - Check **Services** for bulk options and future updates.

    🧠 Let's breathe better — together.
    """)


elif page == "about":
    st.title("About This Project")
    
    st.markdown("""
    ### 🌫️ What is AQI?
    The **Air Quality Index (AQI)** is a standardized system to measure and report daily air quality levels. It indicates how clean or polluted the air is, and what associated health effects might be a concern for you. AQI values are calculated using several pollutants, such as:
    - Particulate Matter (**PM2.5**, **PM10**)
    - **NO₂** (Nitrogen Dioxide)
    - **SO₂** (Sulfur Dioxide)
    - **CO** (Carbon Monoxide)
    - **O₃** (Ozone)
    
    """)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://hooversun.com/downloads/42985/download/AdobeStock_400578113.jpeg?cb=40c92116c45b4d968cb93298204f53f1&w=2100&h=",width=450)

    st.markdown("""
    ---
    ### 🧠 What This Project Does
    This project applies **machine learning** to predict the AQI using the pollutant levels as inputs. 
    We use regression models like **Polynomial Regression** and **XGBoost**, trained on historical AQI data. The app has:
    - ✅ A **manual input form** for single predictions
    - 📄 **Bulk prediction** via CSV uploads
    - 📊 Graphical outputs and interactive pages

    """)
    st.image("https://www.researchgate.net/publication/379152313/figure/fig2/AS:11431281230776625@1711080292683/Sample-data-in-air-quality-dataset-for-Delhi-City.png", caption="Pollution Dataset Sample", width=600)

    st.markdown("""
    ### 🎯 Why It Matters
    - 🚨 **Early alerts** for poor air quality
    - 🏥 Supports **public health planning**
    - 🌆 Guides **urban and environmental policy**
    - 📱 Can be extended to mobile apps or real-time dashboards.
                
    This project shows how **data science** can directly contribute to a **safer and healthier world**. 🌍💚
    """)

    st.success("Explore other sections like Prediction, Services, and Contact to learn more!")

elif page == "prediction":
    st.title("AQI Prediction Form")
    with st.form("predict_form"):
        pm25 = st.number_input("PM2.5", min_value=0.0)
        no2 = st.number_input("NO2", min_value=0.0)
        so2 = st.number_input("SO2", min_value=0.0)
        co = st.number_input("CO", min_value=0.0)
        o3 = st.number_input("O3", min_value=0.0)
        submit = st.form_submit_button("Predict")

    if submit:
        result = predict_aqi([pm25, no2, so2, co, o3])
        st.success(f"Predicted AQI: {result:.2f}")

        st.markdown("### 📂 Bulk Prediction from CSV")
    csv = st.file_uploader("Upload CSV with columns: PM2.5, NO2, SO2, CO, O3", type="csv")

    def get_aqi_category(aqi):
        if aqi <= 50:
            return "Good"
        elif aqi <= 100:
            return "Satisfactory"
        elif aqi <= 200:
            return "Moderate"
        elif aqi <= 300:
            return "Poor"
        elif aqi <= 400:
            return "Very Poor"
        else:
            return "Severe"

    if csv:
        df = pd.read_csv(csv)

        # Predict AQI
        df["Predicted AQI"] = df.apply(lambda row: predict_aqi([
            row["PM2.5"], row["NO2"], row["SO2"], row["CO"], row["O3"]
        ]), axis=1)

        # Add AQI Category
        df["Category"] = df["Predicted AQI"].apply(get_aqi_category)

        # Show first few results
        st.markdown("### 🔍 Preview")
        st.dataframe(df.head())

        # Show Summary of Categories
        st.markdown("### 📊 Summary of AQI Categories")
        st.write(df["Category"].value_counts())

        # Download option
        csv_data = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Results as CSV", csv_data, "predicted_aqi.csv", "text/csv")


elif page == "services":
    st.title("🌟 Services We Offer")
    st.markdown("---")

    st.subheader("📈 AQI Prediction (Single Entry)")
    st.write("""
        Predict the **Air Quality Index** using values like PM2.5, NO2, SO2, CO, and O3. 
        Get immediate feedback on whether the air is **Good**, **Moderate**, or **Severe**.
    """)

    st.subheader("📂 Bulk CSV Prediction")
    st.write("""
        Upload a CSV file with pollution data for batch processing. 
        Automatically predicts AQI for each row and categorizes air quality. 
        Results can be downloaded in one click.
    """)

    st.subheader("🌆 Urban Pollution Insights (Coming Soon)")
    st.write("""
        Visualize and compare AQI trends across cities and time using interactive graphs. 
        Useful for urban planning, awareness campaigns, and research.
    """)

    st.image("https://cdn.pixabay.com/photo/2016/01/19/15/05/smog-1149988_1280.jpg", use_container_width=True)


elif page == "contact":
    st.title("📩 Contact")

    st.markdown("### 👩‍💻 Developed By")
    st.markdown("""
    **Name:** Srishti Bhatnagar  
    **Email:** [srishtibhatnagar051@gmail.com](mailto:srishtibhatnagar051@gmail.com)  
    **LinkedIn:** [Srishti Bhatnagar](https://www.linkedin.com/in/srishti-bhatnagar-b59833269)  
    """)

    st.markdown("### 📝 Send Us a Message")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        send = st.form_submit_button("Send")

        if send:
            st.success("✅ Thanks! We'll get back to you soon.")

