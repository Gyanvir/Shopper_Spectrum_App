import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# --------- OPTIONAL Google Drive logic (disabled for now) ---------
# import gdown
# import tempfile
# 
# ITEM_SIM_FILE_ID = "1SQScU2P490qgMM0shRQhTSaSOp_bNBQq"
# temp_dir = tempfile.gettempdir()
# ITEM_SIM_FILENAME = os.path.join(temp_dir, "item_sim_df.pkl")
# 
# if not os.path.exists(ITEM_SIM_FILENAME):
#     gdown.download(f"https://drive.google.com/uc?id={ITEM_SIM_FILE_ID}", ITEM_SIM_FILENAME, quiet=False)

# --------- Local file approach ---------
ITEM_SIM_FILENAME = os.path.join(os.path.dirname(__file__), "item_sim_df.pkl")

# ---- Page Config ----
st.set_page_config(page_title="Shopper Spectrum - Retail Intelligence", layout="centered")

# ---- Load Models ----
kmeans = joblib.load(os.path.join(os.path.dirname(__file__), "rfm_model.pkl"))
scaler = joblib.load(os.path.join(os.path.dirname(__file__), "scaler.pkl"))
item_sim_df = joblib.load(ITEM_SIM_FILENAME)

# ---- Cluster Descriptions ----
cluster_profiles = {
    0: "Customer is a Regular buyer with moderate recent activity and moderate spending.",
    1: "Customer is At-Risk with long inactivity and low purchase frequency.",
    2: "Customer is an Occasional buyer with somewhat regular purchases and decent spending.",
    3: "Customer is a High-Value buyer who purchases frequently, recently, and spends significantly."
}

# ---- UI ----
st.title("Shopper Spectrum: Customer Segmentation and Product Intelligence")
tab1, tab2 = st.tabs(["Customer Segmentation", "Product Recommendation"])

# ---------------------- TAB 1 -------------------------
with tab1:
    st.header("Customer Segmentation")

    rec = st.number_input("Recency (days since last purchase)", min_value=0)
    freq = st.number_input("Frequency (number of purchases)", min_value=1)
    mon = st.number_input("Monetary Value (total spend)", min_value=1)

    if st.button("Predict Customer Category"):
        input_data = np.log1p([[rec, freq, mon]])
        input_scaled = scaler.transform(input_data)
        cluster = int(kmeans.predict(input_scaled)[0])

        st.markdown(f"**Customer belongs to Category {cluster}**")
        st.markdown(f"{cluster_profiles.get(cluster, 'No profile description available.')}")

# ---------------------- TAB 2 -------------------------
with tab2:
    st.header("Product Recommendations")

    product_input = st.text_input("Enter a Product Name (case-sensitive):")

    if st.button("Get Recommendations"):
        if product_input not in item_sim_df.columns:
            st.error("Product not found. Please check for typos or ensure the product exists in the dataset.")
        else:
            recommendations = item_sim_df[product_input].sort_values(ascending=False)[1:6]

            st.subheader("Recommended Products:")
            for i, product in enumerate(recommendations.index, 1):
                st.markdown(f"""
                    <div style='
                        padding: 12px;
                        background-color: #f1f3f4;
                        border: 1px solid #ccc;
                        border-radius: 8px;
                        margin-bottom: 10px;
                        font-weight: 500;
                        color: #222;
                    '>
                        {i}. {product}
                    </div>
                """, unsafe_allow_html=True)
