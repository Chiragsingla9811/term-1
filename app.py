import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Creating a sample dataset for demonstration
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [23, 45, 56, 78, 89]
}

df = pd.DataFrame(data)

# Set up the figure to plot all charts in one shot
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# -------------------- Bar Chart --------------------
axs[0].bar(df['Category'], df['Values'], color='skyblue', edgecolor='black', linewidth=1.2)
axs[0].set_title('Bar Chart of Categories', fontsize=16)
axs[0].set_xlabel('Category', fontsize=12)
axs[0].set_ylabel('Values', fontsize=12)
axs[0].tick_params(axis='x', labelsize=12)
axs[0].tick_params(axis='y', labelsize=12)

# Add values on top of each bar
for i, value in enumerate(df['Values']):
    axs[0].text(i, value + 2, str(value), ha='center', fontsize=12, color='black')

# -------------------- Histogram --------------------
axs[1].hist(df['Values'], bins=5, color='lightgreen', edgecolor='black')
axs[1].set_title('Histogram of Values', fontsize=16)
axs[1].set_xlabel('Values', fontsize=12)
axs[1].set_ylabel('Frequency', fontsize=12)
axs[1].tick_params(axis='x', labelsize=12)
axs[1].tick_params(axis='y', labelsize=12)

# -------------------- Pie Chart --------------------
colors = ['gold', 'lightblue', 'lightcoral', 'lightgreen', 'violet']
axs[2].pie(df['Values'], labels=df['Category'], autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops={'edgecolor': 'black', 'linewidth': 1.2})
axs[2].set_title('Pie Chart of Categories', fontsize=16)

# Adjust layout for clarity
plt.tight_layout()
plt.show()
