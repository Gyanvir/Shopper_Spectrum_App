# 🛍️ Shopper Spectrum: Customer Segmentation & Product Recommendations

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
🔗 **Live Demo**: [Hugging Face Space](https://huggingface.co/spaces/thegyanvirs/shopper-spectrum-app-gyanvirS)

---

## 🚀 About the Project

**Shopper Spectrum** is a two-in-one retail intelligence solution:
- 🧠 **Customer Segmentation** using RFM clustering (Recency, Frequency, Monetary)
- 🎯 **Product Recommendation System** using precomputed item-item similarity matrix

This Streamlit app empowers businesses to:
- Understand customer buying behavior
- Predict loyalty clusters (like High-Value, At-Risk, Occasional)
- Recommend similar products based on any selected item

---

## 🗃️ Repository Structure

```bash
.
├── app.py                    # Streamlit app (local .pkl references)
├── rfm_model.pkl             # Trained KMeans model
├── scaler.pkl                # StandardScaler for RFM features
├── requirements.txt          # Python dependencies
├── submission_notebook.ipynb # EDA, modeling pipeline, final outputs
├── LICENSE                   # MIT License
└── README.md                 # You are here!
```

## 🧠 Models & Data
- 📦 Dataset: Retail CSV from Google Drive [here](https://drive.google.com/file/d/1rzRwxm_CJxcRzfoo9Ix37A2JTlMummY-/view)
- 📊 Similarity Matrix: Precomputed .pkl (~114MB)
- 👉 Download [item_sim_df.pkl](https://drive.google.com/file/d/1HZBH2_b6XJwQ-ZuYhNl80RgARTpp9cry/view?usp=sharing) and place it in the same directory as app.py

- Note: The full ML pipeline (EDA, feature engineering, clustering, item similarity) is documented in submission_notebook.ipynb.

## 📦 Installation (Run Locally)
```
# Clone the repo
git clone https://github.com/Gyanvir/Shopper_Spectrum_App.git
cd Shopper_Spectrum_App

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Download large file manually
# Place item_sim_df.pkl in project root
# https://drive.google.com/file/d/1HZBH2_b6XJwQ-ZuYhNl80RgARTpp9cry/view?usp=sharing

# Run the app
streamlit run app.py
```

## 🧪 Features

# 📈 Customer Segmentation Tab
- Input:
   - Recency (days since last purchase)
   - Frequency (purchase count)
   - Monetary value (total spend)
- Output:
   - Cluster number (0–3)
   - Interpretation (e.g., High-Value, At-Risk)

# 🔍 Product Recommendation Tab
- Input:
   - Free-text Product Name (case-sensitive)
- Output:
   - Top 5 similar products (from item similarity matrix)

## 📜 License
This project is licensed under the MIT License – see the LICENSE file for details.

## 👨‍💻 Author
Developed by Gyanvir Singh
For academic & learning purposes ✨
