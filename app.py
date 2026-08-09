
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

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

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

# Revenue trend
st.subheader("📈 Revenue Trend")

revenue_by_date = df.groupby("Date", as_index=False)["Revenue"].sum()

fig = px.line(
    revenue_by_date,
    x="Date",
    y="Revenue",
    markers=True,
    title="Revenue Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Revenue",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

# Sales data
st.subheader("Sales Data")
st.dataframe(df, use_container_width=True)


