
import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Sales & Revenue Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Sales & Revenue Dashboard")
st.write("Analyze sales, revenue, products, and regions.")

# Load data
df = pd.read_csv("sales_data.csv")

# Calculate KPIs
total_sales = df["Sales"].sum()
total_revenue = df["Revenue"].sum()
total_quantity = df["Quantity"].sum()

# KPI cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Total Sales", f"₹{total_sales:,.0f}")

with col2:
    st.metric("📈 Total Revenue", f"₹{total_revenue:,.0f}")

with col3:
    st.metric("📦 Total Quantity", f"{total_quantity:,}")

# Show data
st.subheader("Sales Data")
st.dataframe(df, use_container_width=True)
