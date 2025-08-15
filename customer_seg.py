import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from datetime import datetime

# 1. Load dataset
df = pd.read_csv("D:\kaggle dataset\online_retail.csv",header=0)

# 2. Remove null CustomerID
df.dropna(subset=['CustomerID'], inplace=True)

# 3. Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True, errors='coerce')

# 4. Calculate Recency, Frequency, Monetary
# Reference date is one day after the last purchase in dataset
reference_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (reference_date - x.max()).days,  # Recency
    'InvoiceNo': 'nunique',  # Frequency
    'UnitPrice': 'sum'       # Monetary (simple version)
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

# 5. K-Means Clustering
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm)

# 6. Show cluster counts
print(rfm.groupby('Cluster').mean())

# 7. Plot clusters
plt.scatter(rfm['Recency'], rfm['Monetary'], c=rfm['Cluster'], cmap='viridis')
plt.xlabel('Recency (days)')
plt.ylabel('Monetary')
plt.title('Customer Segmentation')
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(rfm["Recency"], rfm["Monetary"], 
            c=rfm["Cluster"], cmap="viridis", alpha=0.6, edgecolors='k')

plt.xlabel("Recency (days)")
plt.ylabel("Monetary Value")
plt.title("Customer Segmentation (Recency vs Monetary)")
plt.colorbar(label='Cluster')
plt.show()