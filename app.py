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

# Set the page layout to wide for better visualization
st.set_page_config(layout="wide")

# Dashboard title
st.title("Data Visualization Dashboard")

# Layout for Cross-sectional Data visualizations
st.subheader("Cross-sectional Data")

col1, col2, col3 = st.columns(3)

# Scatter Plot for Cross-sectional Data with a colorful palette
with col1:
    fig_scatter = px.scatter(cross_sectional_data, x='X', y='Y', text='Entity', title="Scatter Plot (Cross-sectional)",
                             color='Entity', color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_scatter)

# Bar Chart for Cross-sectional Data with a vibrant palette
with col2:
    fig_bar = px.bar(cross_sectional_data, x='Entity', y='Y', title="Bar Chart (Cross-sectional)",
                     color='Entity', color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(fig_bar)

# Line Chart for Cross-sectional Data with a rainbow color scheme
with col3:
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=cross_sectional_data['X'], y=cross_sectional_data['Y'],
                                  mode='lines+markers', line=dict(color='firebrick', width=4), name="Line Chart"))
    fig_line.update_layout(title="Line Chart (Cross-sectional)", template="plotly_dark")
    st.plotly_chart(fig_line)

# Layout for Time-series Data visualizations
st.subheader("Time-series Data")

col4, col5, col6 = st.columns(3)

# Line Chart for Time-series Data with a colorful palette
with col4:
    fig_ts_line = px.line(time_series_data, x='Time', y='Y', title="Line Chart (Time-series)",
                          color_discrete_sequence=px.colors.sequential.Plasma)
    st.plotly_chart(fig_ts_line)

# Scatter Plot for Time-series Data with a deep color palette
with col5:
    fig_ts_scatter = px.scatter(time_series_data, x='Time', y='Y', title="Scatter Plot (Time-series)",
                                color_discrete_sequence=px.colors.sequential.Agsunset)
    st.plotly_chart(fig_ts_scatter)

# Bar Chart for Time-series Data with a vivid palette
with col6:
    fig_ts_bar = px.bar(time_series_data, x='Time', y='Y', title="Bar Chart (Time-series)",
                        color_discrete_sequence=px.colors.qualitative.Bold)
    st.plotly_chart(fig_ts_bar)

# Layout for Panel Data visualizations
st.subheader("Panel Data")

col7, col8, col9 = st.columns(3)

# Line Chart for Panel Data with a bright palette
with col7:
    fig_panel_line = px.line(panel_data, x='Time', y='Y', color='Entity', title="Line Chart (Panel Data)",
                             color_discrete_sequence=px.colors.qualitative.Dark2)
    st.plotly_chart(fig_panel_line)

# Scatter Plot for Panel Data with a pastel color palette
with col8:
    fig_panel_scatter = px.scatter(panel_data, x='Time', y='Y', color='Entity', title="Scatter Plot (Panel Data)",
                                   color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_panel_scatter)

# Bar Chart for Panel Data with a bold palette
with col9:
    fig_panel_bar = px.bar(panel_data, x='Time', y='Y', color='Entity', barmode='group', title="Bar Chart (Panel Data)",
                           color_discrete_sequence=px.colors.qualitative.Prism)
    st.plotly_chart(fig_panel_bar)
