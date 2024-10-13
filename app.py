import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (replace this path with the actual dataset path)
# Assuming the file is uploaded or you are reading it locally
data = pd.read_csv('Imports_Exports_Dataset.csv')

# Display the title and dataset
st.title("Trade Data Visualization Dashboard")
st.write("This dashboard provides visualizations for Exports, Imports, and Trade Balance by Country.")

# Display the dataset
st.subheader("Dataset")
st.write(data)

# Set up the figure for enhanced visualizations
st.subheader("Visualizations")

# Create a 2x2 grid for displaying charts
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# -------------------- Bar Chart for Exports --------------------
sns.barplot(x='Country', y='Exports', data=data, palette='Blues_d', ax=axs[0, 0])
axs[0, 0].set_title('Country-wise Exports', fontsize=14)
axs[0, 0].set_xlabel('Country', fontsize=10)
axs[0, 0].set_ylabel('Exports (in billion $)', fontsize=10)
axs[0, 0].tick_params(axis='x', rotation=45)

# -------------------- Bar Chart for Imports --------------------
sns.barplot(x='Country', y='Imports', data=data, palette='Greens_d', ax=axs[0, 1])
axs[0, 1].set_title('Country-wise Imports', fontsize=14)
axs[0, 1].set_xlabel('Country', fontsize=10)
axs[0, 1].set_ylabel('Imports (in billion $)', fontsize=10)
axs[0, 1].tick_params(axis='x', rotation=45)

# -------------------- Pie Chart for Trade Balance --------------------
colors = sns.color_palette('pastel')
axs[1, 0].pie(data['Trade_Balance'], labels=data['Country'], autopct='%1.1f%%', startangle=90, colors=colors)
axs[1, 0].set_title('Trade Balance Distribution by Country', fontsize=14)

# -------------------- Scatter Plot for Exports vs Imports --------------------
axs[1, 1].scatter(data['Exports'], data['Imports'], color='purple', s=100)
for i, txt in enumerate(data['Country']):
    axs[1, 1].annotate(txt, (data['Exports'][i], data['Imports'][i]), fontsize=10, ha='right')
axs[1, 1].set_title('Scatter Plot of Exports vs Imports', fontsize=14)
axs[1, 1].set_xlabel('Exports (in billion $)', fontsize=10)
axs[1, 1].set_ylabel('Imports (in billion $)', fontsize=10)

# Adjust layout for better spacing
plt.tight_layout()

# Show the visualizations in Streamlit
st.pyplot(fig)
