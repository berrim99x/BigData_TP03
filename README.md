# 📊 Sales Data Analysis Project using Python & Power BI

## 🚀 Project Overview

This project presents a complete **data analysis workflow** using **Python 🐍** and **Power BI 📊**.

The goal of the project is to analyze sales data in order to extract valuable insights about:

* 📦 Product performance
* 🌍 Regional sales distribution
* 👥 Customer behavior

The project demonstrates the **full data analysis pipeline**, including:

* 🧾 Data generation
* 🧹 Data cleaning & preprocessing
* 🔎 Exploratory Data Analysis (EDA)
* 🤖 Customer segmentation using Machine Learning
* 📊 Interactive visualization using Power BI

---

# 📁 Project Structure

```text
TP03_Full_Data_Analysis
│
├── data
│   └── sales_data.csv
│
├── src
│   ├── data_cleaning.py
│   ├── eda.py
│   └── analysis.py
│
├── generate_data.py
├── main.py
├── cleaned_sales_data.csv
├── dashboard.png
└── README.md
```

---

# 📦 Dataset Description

The dataset contains **simulated sales transactions**.

Each record includes the following attributes:

| Column         | Description                |
| -------------- | -------------------------- |
| 📅 date        | Date of the transaction    |
| 📦 product     | Product name               |
| 🌍 region      | Sales region               |
| 👤 customer_id | Unique customer identifier |
| 💰 sales       | Sales value                |

The dataset intentionally includes:

* ❌ Missing values
* 🔁 Duplicate records
* 📈 Outliers

This helps demonstrate **real-world data cleaning techniques**.

---

# 🧹 Data Cleaning

Data preprocessing was performed using the **Pandas** library.

The following operations were applied:

* ❌ Removing missing values
* 🔁 Removing duplicate records
* 📅 Converting the date column to datetime format
* 🧮 Preparing the dataset for analysis

The cleaned dataset is saved as:

```text
cleaned_sales_data.csv
```

---

# 🔎 Exploratory Data Analysis (EDA)

EDA was performed to better understand the dataset.

The following analyses were conducted:

* 📊 Descriptive statistics
* 🔗 Correlation analysis
* 📈 Sales trends over time

Python libraries used:

* 🐼 Pandas
* 📉 Matplotlib
* 🎨 Seaborn

---

# 🤖 Customer Segmentation

Customer segmentation was performed using the **K-Means Clustering algorithm**.

Customers were divided into three groups:

| Cluster | Customer Type          |
| ------- | ---------------------- |
| 🟢 0    | High-value customers   |
| 🟡 1    | Medium-value customers |
| 🔴 2    | Low-value customers    |

This helps businesses identify their **most valuable customers**.

---

# 📊 Power BI Dashboard

An interactive **Power BI dashboard** was created to visualize the results.

The dashboard includes:

* 💰 Total Sales KPI
* 📊 Average Sales KPI
* 👥 Total Customers KPI
* 📦 Sales by Product
* 🌍 Sales by Region
* 🤖 Customer Segmentation
* 📈 Sales Trends Over Time
* 🎛 Interactive filters (Slicers)

Dashboard Preview:

![Dashboard](dashboard.png)

---

# 🛠 Technologies Used

This project uses the following tools and technologies:

* 🐍 Python
* 🐼 Pandas
* 🔢 NumPy
* 📉 Matplotlib
* 🎨 Seaborn
* 🤖 Scikit-learn
* 📊 Power BI

---

# 📌 Key Insights

The analysis revealed several important insights:

* 📦 Sales are distributed across different product categories.
* 🌍 Some regions generate higher revenue than others.
* 👥 A small group of customers contributes significantly to total sales.
* 🎯 Customer segmentation helps businesses target high-value customers.

---

# 👨‍💻 Author

**Abdelhakim Berrim**

🎓 Data Analysis Project
🐍 Python & 📊 Power BI
