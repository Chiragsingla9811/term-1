import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# -------------------- Data Creation (Cross-sectional, Time-series, Panel Data) --------------------

np.random.seed(0)

# 1. Cross-sectional data (multiple entities at one time point)
cross_sectional_data = pd.DataFrame({
    'Entity': ['A', 'B', 'C', 'D', 'E'],
    'X': np.random.rand(5),
    'Y': np.random.rand(5) * 10
})

# 2. Time-series data (single entity tracked over time)
time_series_data = pd.DataFrame({
    'Time': pd.date_range(start='2020-01-01', periods=10, freq='ME'),
    'X': np.random.rand(10),
    'Y': np.random.rand(10) * 20
})

# 3. Panel data (multiple entities tracked over time)
panel_data = pd.DataFrame({
    'Entity': ['A'] * 5 + ['B'] * 5,
    'Time': list(pd.date_range(start='2020-01-01', periods=5, freq='ME')) * 2,
    'X': np.random.rand(10),
    'Y': np.random.rand(10) * 30
})

# -------------------- Streamlit Dashboard --------------------

# Dashboard title
st.title("Interactive Data Visualization Dashboard")

# Sidebar for Data Selection
st.sidebar.title("Options")
data_type = st.sidebar.selectbox("Select Dataset", ["Cross-sectional", "Time-series", "Panel Data"])

# Chart type selection
chart_type = st.sidebar.selectbox("Select Chart Type", ["Line Chart", "Scatter Plot", "Bar Chart"])

# Filter options for panel data
if data_type == "Panel Data":
    entities = st.sidebar.multiselect("Select Entities", options=panel_data['Entity'].unique(), default=panel_data['Entity'].unique())

# Cross-sectional Data Visualization
if data_type == "Cross-sectional":
    st.subheader("Cross-sectional Data")
    st.write(cross_sectional_data)

    # Plot based on selected chart type
    if chart_type == "Scatter Plot":
        fig = px.scatter(cross_sectional_data, x='X', y='Y', text='Entity', title="Scatter Plot of Cross-sectional Data")
    elif chart_type == "Bar Chart":
        fig = px.bar(cross_sectional_data, x='Entity', y='Y', title="Bar Chart of Cross-sectional Data")
    elif chart_type == "Line Chart":
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=cross_sectional_data['X'], y=cross_sectional_data['Y'], mode='lines+markers'))
        fig.update_layout(title="Line Chart of Cross-sectional Data")

    st.plotly_chart(fig)

# Time-series Data Visualization
elif data_type == "Time-series":
    st.subheader("Time-series Data")
    st.write(time_series_data)

    # Plot based on selected chart type
    if chart_type == "Line Chart":
        fig = px.line(time_series_data, x='Time', y='Y', title="Line Chart of Time-series Data")
    elif chart_type == "Scatter Plot":
        fig = px.scatter(time_series_data, x='Time', y='Y', title="Scatter Plot of Time-series Data")
    elif chart_type == "Bar Chart":
        fig = px.bar(time_series_data, x='Time', y='Y', title="Bar Chart of Time-series Data")

    st.plotly_chart(fig)

# Panel Data Visualization
elif data_type == "Panel Data":
    st.subheader("Panel Data")
    filtered_panel_data = panel_data[panel_data['Entity'].isin(entities)]
    st.write(filtered_panel_data)

    # Plot based on selected chart type
    if chart_type == "Line Chart":
        fig = px.line(filtered_panel_data, x='Time', y='Y', color='Entity', title="Line Chart of Panel Data")
    elif chart_type == "Scatter Plot":
        fig = px.scatter(filtered_panel_data, x='Time', y='Y', color='Entity', title="Scatter Plot of Panel Data")
    elif chart_type == "Bar Chart":
        fig = px.bar(filtered_panel_data, x='Time', y='Y', color='Entity', barmode='group', title="Bar Chart of Panel Data")

    st.plotly_chart(fig)
