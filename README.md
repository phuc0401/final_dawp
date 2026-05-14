# Store Revenue Prediction - Data Analysis with Python

## 📌 Project Overview
This repository contains the final group project (Project No. 30) for the Data Analysis with Python course. The objective is to define a meaningful real-world data analysis problem and predict store revenue using machine learning techniques. This is framed as a regression problem, with the primary target variable being Revenue / Sales. 

## 📊 Dataset
[span_0](start_span)[span_1](start_span)We utilized the **Store Sales Time Series Forecasting** dataset from Kaggle[span_0](end_span)[span_1](end_span).
* **Source:** [Kaggle Competition Link](https://www.kaggle.com/competitions/store-sales-time-series-forecast)
* **Components Used:** The dataset is rich and relational, requiring the integration of multiple files including `train.csv`, `stores.csv`, `oil.csv`, `holidays_events.csv`, and `transactions.csv`.

## 🎯 Project Objectives
Throughout this project, our team aimed to:
* [span_2](start_span)Collect, understand, clean, and preprocess a complex multi-table dataset[span_2](end_span).
* [span_3](start_span)Perform comprehensive Exploratory Data Analysis (EDA) and create useful visualizations[span_3](end_span).
* [span_4](start_span)[span_5](start_span)Build at least one baseline model and compare it with another suitable machine learning algorithm[span_4](end_span)[span_5](end_span).
* [span_6](start_span)Evaluate model performance, explain the results, and present the final findings clearly in written and oral form[span_6](end_span).

## 🚀 Workflow & Methodology

1.  **Data Integration & Cleaning:** Merged 5 separate datasets (`train`, `stores`, `oil`, `holidays`, `transactions`) into a single cohesive dataframe based on the `Date` column. [span_7](start_span)Addressed missing values, specifically using **interpolation** to handle weekend gaps in `oil.csv` prices[span_7](end_span).
2.  **Exploratory Data Analysis (EDA):** Analyzed revenue trends spanning from 2013 to 2017 using line charts. [span_8](start_span)Investigated the impact of holidays on sales through bar chart visualizations to extract actionable business insights[span_8](end_span).
3.  **Feature Engineering:** Transformed raw dates into meaningful variables (Year, Month, Day, Is_Weekend, Is_Payday). [span_9](start_span)Created advanced time-series variables including **Lag Features** (e.g., 7-day and 30-day prior revenue) to capture temporal dependencies[span_9](end_span).
4.  **[span_10](start_span)Modeling:** Built a baseline **Decision Tree** model as required, followed by an advanced algorithm (**Random Forest / XGBoost**) for performance comparison[span_10](end_span).
5.  **Evaluation:** Compared models using strict metrics such as RMSE and R-squared. [span_11](start_span)Visualized the final results using Actual vs. Predicted plots to detect signs of underfitting or overfitting[span_11](end_span).

## 📈 Results & Evaluation
*(Note: Update this section with your team's actual findings)*
* **Best Performing Model:** vs code

## 📁 Repository Structure
* [span_12](start_span)`notebook.ipynb`: The main comprehensive Jupyter Notebook combining all code, executing seamlessly from data ingestion to model evaluation[span_12](end_span).
* [span_13](start_span)[span_14](start_span)`report.pdf`: The detailed project report covering Introduction to Conclusion (Sections 1-8)[span_13](end_span)[span_14](end_span).
* [span_15](start_span)`presentation_slides.pdf`: 10-15 slides summarizing the problem, data, methodology, results, and conclusion[span_15](end_span).

## 👥 Team Members & Roles

[span_16](start_span)Our team divided the workload to leverage each member's strengths while ensuring everyone understood the full end-to-end pipeline[span_16](end_span):

| Member Name | Role & Core Responsibilities |
| :--- | :--- |
| **[Vu Hoang Quan]** | **Data Builder (Integration & Cleaning):** Ingested and merged the 5 core datasets (`train`, `stores`, `oil`, `holidays`, `transactions`) on the Date column. Handled missing data, notably applying interpolation for missing weekend oil prices. |
| **[Le Trieu Quang Minh]** | **Data Analyst (EDA & Initial Reporting):** Conducted EDA on the merged dataset. Created line charts for 2013-2017 revenue trends and bar charts to analyze holiday impacts. Authored Sections 1 to 4 of the PDF report. |
| **[Nguyen Minh Chien]** | **Feature Engineer:** Extracted temporal features (`Year`, `Month`, `Day`, `Is_Weekend`, `Is_Payday`) from datetime formats. Engineered advanced lag features (7-day and 30-day revenue lags) to optimize the dataset for machine learning. |
| **[Duong Huy Phuc]** | **Machine Learning Engineer:** Utilized the engineered dataset to train a baseline Decision Tree model and an advanced model (Random Forest/XGBoost). Calculated RMSE and R² scores, and plotted Actual vs. Predicted graphs. |
| **[Ta Quang Huy]** | **Project Manager:** Consolidated individual codes into a single, smooth-running Jupyter Notebook. Authored Sections 5 to 8 of the report, designed presentation slides, managed the GitHub repository, and delivered the video presentation. |

## 🔗 Links
* **[span_18](start_span)Kaggle Dataset:** [Link](https://www.kaggle.com/competitions/store-sales-time-series-forecasting)[span_18](end_span)
* **[span_19](start_span)GitHub Repository:** [Insert Link Here][span_19](end_span)

---
*This project strictly adheres to academic integrity guidelines. [span_20](start_span)All external references and datasets are cited clearly, and no unverified AI-generated code or copied work was used without understanding[span_20](end_span).*
