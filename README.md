# Shopper Spectrum: Customer Segmentation and Recommendations

This Streamlit app provides:
- Customer segmentation using RFM analysis and KMeans clustering
- Product recommendations using item-item collaborative filtering

## Features

1. **Customer Segmentation**
   - Input: Recency, Frequency, Monetary values
   - Output: Customer cluster category (High-Value, Occasional, At-Risk, etc.)

2. **Product Recommendations**
   - Input: Product name (text)
   - Output: Top 5 similar products based on purchase behavior

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
## Deployment
Deployed on Streamlit Cloud- 

## Project Structure
├── app.py
├── rfm_model.pkl
├── scaler.pkl
├── item_sim_df.pkl
├── requirements.txt
└── README.md

## Dataset Source
Online_Retail.csv- https://drive.google.com/file/d/1rzRwxm_CJxcRzfoo9Ix37A2JTlMummY-/view?usp=sharing





