import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'revenue': [12000, 15000, 14000, 19000, 22000, 21000, 25000, 28000, 27000, 32000, 35000, 40000],
    'marketing_spend': [1000, 1500, 1200, 2000, 2500, 2200, 3000, 3500, 3200, 4000, 4500, 5000],
    'profit': [5000, 6000, 5500, 8000, 9500, 9000, 11000, 12500, 12000, 14500, 16000, 18500]
}

df = pd.DataFrame(data)

plt.plot(df['month'], df['revenue'], marker='o', color='b', linestyle='-')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.grid(True)
plt.savefig('revenue_trend.png')
plt.close()

plt.scatter(df['marketing_spend'], df['profit'], color='r')
plt.title('Marketing Spend vs Profit')
plt.xlabel('Marketing Spend ($)')
plt.ylabel('Profit ($)')
plt.grid(True)
plt.savefig('marketing_vs_profit.png')
plt.close()

numeric_df = df[['revenue', 'marketing_spend', 'profit']]
correlation = numeric_df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Map')
plt.savefig('correlation_map.png')
plt.close()