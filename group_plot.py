import pandas as pd
import matplotlib.pyplot as plt

# CSV लोड करें
df = pd.read_csv('sales.csv')

# Group by Region और Sales का sum निकालें
grouped = df.groupby('Region')['Sales'].sum()

# Print करें
print(grouped)

# Plot करें
grouped.plot(kind='bar', title='Total Sales by Region', color='skyblue')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()
