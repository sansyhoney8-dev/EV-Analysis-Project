import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_dashboard():
    # 1. Connect to your existing DB
    conn = sqlite3.connect('ev_performance.db')
    df = pd.read_sql_query("SELECT * FROM ev_data", conn)
    conn.close()

    # 2. Set the style for professional-looking graphs
    sns.set_theme(style="darkgrid")
    
    # 3. Create a figure with 3 subplots (1 row, 3 columns)
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))
    fig.suptitle('Electric Vehicle Data Analysis Dashboard', fontsize=20)

    # --- Graph 1: Bar Chart (Top Models by Range) ---
    avg_range = df.groupby('model')['range'].mean().sort_values(ascending=False)
    sns.barplot(x=avg_range.values, y=avg_range.index, ax=axes[0], palette="magma")
    axes[0].set_title('Average Range per Model')
    axes[0].set_xlabel('Range (km)')

    # --- Graph 2: Scatter Plot (Battery vs. Range Correlation) ---
    # We use a sample of 1000 so the graph is clear
    sns.scatterplot(data=df.sample(1000), x='battery', y='range', hue='model', ax=axes[1])
    axes[1].set_title('Battery Capacity vs. Total Range')
    axes[1].set_xlabel('Battery (kWh)')

    # --- Graph 3: Box Plot (Range Distribution) ---
    sns.boxplot(data=df, x='range', y='model', ax=axes[2], palette="Set2")
    axes[2].set_title('Range Distribution across Models')

    # 4. Save and Show
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('ev_final_graphs.png')
    print("Graphs generated successfully and saved as 'ev_final_graphs.png'")
    plt.show()

if __name__ == "__main__":
    create_dashboard()
