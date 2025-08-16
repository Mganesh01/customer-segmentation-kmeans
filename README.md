🛒 Customer Segmentation using K-Means
📌 Project Overview

This project applies clustering techniques (K-Means) to perform customer segmentation on a retail dataset.
By analyzing customer purchasing behavior using RFM (Recency, Frequency, Monetary) metrics, we can identify distinct groups of customers such as:

VIP High Spenders

Frequent Buyers

Occasional Shoppers

Low Value Customers

This segmentation helps businesses design targeted marketing strategies and improve customer retention.

📂 Dataset

Source: Online Retail Dataset (Kaggle)

Description:

Transactions of a UK-based online retailer

Features: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

⚙️ Steps Performed

Data Preprocessing

Removed missing Customer IDs

Converted InvoiceDate to datetime format

Feature Engineering (RFM Analysis)

Recency → Days since last purchase

Frequency → Number of purchases

Monetary → Total spend by customer

Clustering (K-Means)

Applied K-Means algorithm with 4 clusters

Segmented customers based on RFM scores

Visualization

Scatter plots of Recency vs Monetary

Cluster distribution analysis

📊 Results

Identified 4 customer segments

Example groups:

Cluster 0 → VIP Customers (Frequent + High spenders)

Cluster 1 → Occasional Buyers

Cluster 2 → Rare Shoppers

Cluster 3 → Low Value Customers
