import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Sample dataset for demonstration (replace this with your actual data)
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [23, 45, 56, 78, 89]
}
df = pd.DataFrame(data)

# Sample time-series data
time_series_data = pd.DataFrame({
    'Date': pd.date_range(start='2021-01-01', periods=100, freq='D'),
    'Values': np.random.randn(100).cumsum()
})

# Panel-like data
panel_data = pd.DataFrame({
    'Entity': ['A'] * 10 + ['B'] * 10,
    'Time': pd.date_range(start='2021-01-01', periods=10, freq='M').tolist() * 2,
    'Values': np.random.rand(20) * 100
})

# Streamlit Dashboard
st.title("Interactive Data Visualization Dashboard")

# Display all charts together for categorical data
st.header("Categorical Data Visualizations")

# Bar chart
st.subheader("Bar Chart")
bar_chart = px.bar(df, x='Category', y='Values', title="Bar Chart")
st.plotly_chart(bar_chart)

# Pie chart
st.subheader("Pie Chart")
pie_chart = px.pie(df, values='Values', names='Category', title="Pie Chart")
st.plotly_chart(pie_chart)

# Display all charts together for time-series data
st.header("Time-series Data Visualizations")

# Line chart
st.subheader("Line Chart")
line_chart = px.line(time_series_data, x='Date', y='Values', title="Time-series Line Chart")
st.plotly_chart(line_chart)

# Histogram for time-series values
st.subheader("Histogram")
hist_chart = px.histogram(time_series_data, x='Values', nbins=20, title="Time-series Histogram")
st.plotly_chart(hist_chart)

# Panel data visualizations
st.header("Panel Data Visualizations")

# Line chart by entity
st.subheader("Line Chart by Entity")
panel_line_chart = px.line(panel_data, x='Time', y='Values', color='Entity', title="Panel Data Line Chart")
st.plotly_chart(panel_line_chart)

# Scatter plot by entity
st.subheader("Scatter Plot by Entity")
panel_scatter_chart = px.scatter(panel_data, x='Time', y='Values', color='Entity', title="Panel Data Scatter Plot")
st.plotly_chart(panel_scatter_chart)
