import streamlit as st
import pandas as pd
import numpy as np
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

# Displaying all charts together for Cross-sectional Data
st.header("Cross-sectional Data")
st.write(cross_sectional_data)

# Scatter Plot for Cross-sectional Data
st.subheader("Scatter Plot")
fig_scatter = px.scatter(cross_sectional_data, x='X', y='Y', text='Entity', title="Cross-sectional Data: Scatter Plot")
st.plotly_chart(fig_scatter)

# Bar Chart for Cross-sectional Data
st.subheader("Bar Chart")
fig_bar = px.bar(cross_sectional_data, x='Entity', y='Y', title="Cross-sectional Data: Bar Chart")
st.plotly_chart(fig_bar)

# Line Chart for Cross-sectional Data
st.subheader("Line Chart")
fig_line = go.Figure()
fig_line.add_trace(go.Scatter(x=cross_sectional_data['X'], y=cross_sectional_data['Y'], mode='lines+markers'))
fig_line.update_layout(title="Cross-sectional Data: Line Chart")
st.plotly_chart(fig_line)

# Displaying all charts together for Time-series Data
st.header("Time-series Data")
st.write(time_series_data)

# Line Chart for Time-series Data
st.subheader("Line Chart")
fig_ts_line = px.line(time_series_data, x='Time', y='Y', title="Time-series Data: Line Chart")
st.plotly_chart(fig_ts_line)

# Scatter Plot for Time-series Data
st.subheader("Scatter Plot")
fig_ts_scatter = px.scatter(time_series_data, x='Time', y='Y', title="Time-series Data: Scatter Plot")
st.plotly_chart(fig_ts_scatter)

# Bar Chart for Time-series Data
st.subheader("Bar Chart")
fig_ts_bar = px.bar(time_series_data, x='Time', y='Y', title="Time-series Data: Bar Chart")
st.plotly_chart(fig_ts_bar)

# Displaying all charts together for Panel Data
st.header("Panel Data")
st.write(panel_data)

# Line Chart for Panel Data
st.subheader("Line Chart (Entity-wise)")
fig_panel_line = px.line(panel_data, x='Time', y='Y', color='Entity', title="Panel Data: Line Chart")
st.plotly_chart(fig_panel_line)

# Scatter Plot for Panel Data
st.subheader("Scatter Plot (Entity-wise)")
fig_panel_scatter = px.scatter(panel_data, x='Time', y='Y', color='Entity', title="Panel Data: Scatter Plot")
st.plotly_chart(fig_panel_scatter)

# Bar Chart for Panel Data
st.subheader("Bar Chart (Entity-wise)")
fig_panel_bar = px.bar(panel_data, x='Time', y='Y', color='Entity', barmode='group', title="Panel Data: Bar Chart")
st.plotly_chart(fig_panel_bar)
