import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

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

# -------------------- Streamlit App --------------------

# Title
st.title("Data Visualization App")

# Sidebar for Data Selection
st.sidebar.title("Select Data Type")
data_type = st.sidebar.selectbox("Choose the type of data to visualize", 
                                 ["Cross-sectional", "Time-series", "Panel"])

# Show the selected data
if data_type == "Cross-sectional":
    st.subheader("Cross-sectional Data")
    st.dataframe(cross_sectional_data)

    # Scatter plot for cross-sectional data
    st.subheader("Scatter Plot of Cross-sectional Data")
    fig, ax = plt.subplots()
    ax.scatter(cross_sectional_data['X'], cross_sectional_data['Y'])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    st.pyplot(fig)

elif data_type == "Time-series":
    st.subheader("Time-series Data")
    st.dataframe(time_series_data)

    # Line plot for time-series data
    st.subheader("Line Plot of Time-series Data")
    fig, ax = plt.subplots()
    ax.plot(time_series_data['Time'], time_series_data['Y'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Y')
    st.pyplot(fig)

elif data_type == "Panel":
    st.subheader("Panel Data")
    st.dataframe(panel_data)

    # Line plot for panel data
    st.subheader("Line Plot of Panel Data (Entity-wise)")
    fig, ax = plt.subplots()
    for entity in panel_data['Entity'].unique():
        entity_data = panel_data[panel_data['Entity'] == entity]
        ax.plot(entity_data['Time'], entity_data['Y'], label=f'Entity {entity}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Y')
    ax.legend()
    st.pyplot(fig)

# -------------------- Linear Regression Function --------------------
def linear_regression(X, Y):
    X = sm.add_constant(X)  # Add constant term for intercept
    model = sm.OLS(Y, X).fit()
    return model

# Regression Analysis
st.sidebar.subheader("Regression Analysis")
if st.sidebar.button("Perform Regression on Cross-sectional Data"):
    X = cross_sectional_data[['X']]
    Y = cross_sectional_data['Y']
    model = linear_regression(X, Y)
    
    st.subheader("Regression Results for Cross-sectional Data")
    st.text(model.summary())
    
    # Regression plot
    st.subheader("Regression Line Plot")
    fig, ax = plt.subplots()
    ax.scatter(cross_sectional_data['X'], cross_sectional_data['Y'], label='Data')
    ax.plot(cross_sectional_data['X'], model.predict(sm.add_constant(X)), color='red', label='Regression Line')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    st.pyplot(fig)
