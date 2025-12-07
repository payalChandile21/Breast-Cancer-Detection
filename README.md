# COMP47780 -- Cloud Computing Project

## Healthcare Data Warehouse Management

**Student:** Payal Shashikant Chandile
**Student ID:** 25215994

------------------------------------------------------------------------

## Project 1: Healthcare Data Warehouse Management 

  -----------------------------------------------------------------------
  Requirement         Status      Implementation Details
  ------------------- ----------- ---------------------------------------
  **a. Identify                   Breast Cancer Wisconsin (Diagnostic)
  medical datasets**  Completed   Dataset -- 569 patient records with 32
                                  clinical features (Kaggle)

  **b. Define the                 Clinical decision support system for
  application**       Completed   early breast cancer detection through
                                  tumor pattern analysis

  **c. Choose cloud              **Amazon Athena + Amazon S3** (fully
  data warehouse      Completed   serverless SQL data warehouse using
  solution**                      Presto/Trino over object storage)

  **d. Implement the              \- Created S3 bucket
  medical data        Completed   `breastcancer-warehouse-25215994`
  warehouse**                     
  -----------------------------------------------------------------------

-   Uploaded dataset CSV to Amazon S3\
-   Created Athena database `breastcancer_db`\
-   Created external table `diagnostics` mapped to S3 data\
-   Executed analytical SQL queries directly on the cloud \| \| **e.
    Build a dashboard** \| Completed \| Built a fully interactive
    **Streamlit** dashboard connected live to Amazon Athena \|

------------------------------------------------------------------------

##  LIVE DEPLOYED DASHBOARD

**Access the real-time dashboard here:**\
**https://breast-cancer-detection-8aedbfuopqntcpzme6ann5.streamlit.app/**

------------------------------------------------------------------------

##  Cloud Architecture

    Amazon S3 Bucket
        └── Breast cancer dataset.csv
             ↓
    Amazon Athena (Serverless Data Warehouse)
             ↓   SQL Queries
    Streamlit Web Application
             ↑
     Deployed on Streamlit Community Cloud

------------------------------------------------------------------------

## Dashboard Features

-   KPIs (total patients, malignant count, benign count, malignant %)\
-   Pie chart --- diagnosis distribution\
-   Bar chart --- average tumor radius comparison\
-   Scatter plot --- tumor radius vs texture\
-   Sidebar filter for All / Malignant / Benign cases\
-   Responsive medical-themed UI

------------------------------------------------------------------------

## How to Run Locally

``` bash
pip install streamlit pandas plotly
streamlit run breast_cancer_dashboard.py
```

------------------------------------------------------------------------

## AWS Services Used

-   Amazon S3\
-   Amazon Athena\
-   AWS IAM\
-   Streamlit Community Cloud

------------------------------------------------------------------------

## Dataset Source

Breast Cancer Wisconsin (Diagnostic) Dataset\
https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data

------------------------------------------------------------------------

## Project Summary

A complete production-ready **serverless healthcare data warehouse on
AWS** with real-time analytics and dashboard visualizations.

------------------------------------------------------------------------

**Author:**\
Payal Chandile\
December 2025
