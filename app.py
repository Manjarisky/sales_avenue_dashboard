
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Sales & Revenue Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales & Revenue Dashboard")
st.write("Analyze sales, revenue, products, and regions.")

# Load data
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# -------------------------
# KPI calculations
# -------------------------
total_sales = df["Sales"].sum()
total_revenue = df["Revenue"].sum()
total_quantity = df["Quantity"].sum()

# -------------------------
# KPI cards
# -------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Total Sales", f"₹{total_sales:,.0f}")

with col2:
    st.metric("📈 Total Revenue", f"₹{total_revenue:,.0f}")

with col3:
    st.metric("📦 Total Quantity", f"{total_quantity:,}")

# -------------------------
# Revenue Trend
# -------------------------
st.subheader("📈 Revenue Trend")

revenue_by_date = df.groupby("Date", as_index=False)["Revenue"].sum()

fig_revenue = px.line(
    revenue_by_date,
    x="Date",
    y="Revenue",
    markers=True,
    title="Revenue Over Time"
)

fig_revenue.update_layout(
    xaxis_title="Date",
    yaxis_title="Revenue",
    hovermode="x unified"
)

st.plotly_chart(fig_revenue, use_container_width=True)

# -------------------------
# Top Performing Products
# -------------------------
st.subheader("🏆 Top-Performing Products")

product_sales = (
    df.groupby("Product", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

fig_products = px.bar(
    product_sales,
    x="Product",
    y="Sales",
    title="Sales by Product",
    text="Sales"
)

fig_products.update_layout(
    xaxis_title="Product",
    yaxis_title="Sales"
)

st.plotly_chart(fig_products, use_container_width=True)

# -------------------------
# Sales Data
# -------------------------
st.subheader("Sales Data")
st.dataframe(df, use_container_width=True)



