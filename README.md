
# Customer Segmentation Analysis




## Project Overview

Customer Segmentation Analysis is a data-driven project designed to categorize customers into distinct groups based on their purchasing behaviors and demographic information. By leveraging K- Means clustering algorithm , this project aims to identify patterns within the customer data that can help businesses tailor their marketing strategies, improve customer retention, and enhance overall customer satisfaction.

## Objectives

○  Identify distinct customer segments: Use clustering techniques to group customers based on various features such as age, income, spending habits, and gender.

○ Analyze customer behavior: Understand the characteristics of each segment to gain insights into different customer profiles.

○ Develop a predictive model: Build a model that can predict the segment a new customer belongs to based on their input features.

○ Deploy the model: Create a Flask-based web application that allows users to input customer data and receive a segmentation prediction in real-time.

## Key Features
⦿ Data Preprocessing: Handling missing values, encoding categorical variables, and standardizing features.

⦿ Clustering Analysis: Implementing K-Means  algorithm to identify customer segments.

![Customer Segmentation Diagram](images/Elbow_Method.png)


⦿ Dimensionality Reduction: Using PCA (Principal Component Analysis) to visualize high-dimensional data in a 2D or 3D space.

![Customer Segmentation Diagram](images/PCA.png)

⦿ Outlier Detection: Identifying and removing outliers to improve the accuracy of the clustering.

⦿Web Application: A Flask application that allows users to input customer data and view the predicted customer segment.

![Customer Segmentation Diagram](images/Flask_web_app.png)


⦿ Visualization: Interactive plots and graphs to visualize the clusters and customer profiles.

![Customer Segmentation Diagram](images/Heatmap.png)

![Customer Segmentation Diagram](images/Cluster_distribution.png)

##  Mathematical Hypothesis Based on the Heatmap Analysis

### Dependency of Spending Score on Age:

**Hypothesis H₁:** Spending Score (S) is positively correlated with Age (A) more strongly than with other factors. This suggests that as Age increases, Spending Score tends to increase or decrease in a consistent manner.

### Gender-Based Influence on Spending Score:

**Hypothesis H₂:** Spending Score (S) has equal but opposite dependencies on the binary gender variables Male (G_M) and Female (G_F):

- For Male (G_M), the correlation with Spending Score is direct: S ∝ G_M.
- For Female (G_F), the correlation with Spending Score is inverse: S ∝ -G_F.

**Equality of Magnitude:** The magnitude of correlation is identical for both genders, indicating that the effect size is the same but in opposite directions:

If S = k × G_M, then S = -k × G_F,

where k is a constant.

## Analysis of Customer Clusters

| Cluster | Age       | Annual Income (k$) | Spending Score (1-100) | Gender_Female | Gender_Male |
|---------|-----------|-------------------|------------------------|---------------|-------------|
| 0       | 49.437500 | 62.416667          | 29.208333               | 0.0           | 1.0         |
| 1       | 28.392857 | 60.428571          | 68.178571               | 1.0           | 0.0         |
| 2       | 47.803571 | 58.071429          | 34.875000               | 1.0           | 0.0         |
| 3       | 28.250000 | 62.000000          | 71.675000               | 0.0           | 1.0         |

### Cluster 0
The Average Age is around 49 years , Average Annual Income is around 62.4 k$ , average spending score is around 29 and all customers in this cluster seems to be Male.

### Cluster 1
The Average Age is around 28 years , Average Annual Income is around 60.4 k$ , average spending score is around 68 and all customers in this cluster seems to be Female.

### Cluster 2
The Average Age is around 47 years , Average Annual Income is around 58 k$ , average spending score is around 34 and all customers in this cluster seems to be Female.

### Cluster 3
The Average Age is around 28 years , Average Annual Income is around 62 k$ , average spending score is around 71 and all customers in this cluster seems to be Male.


## Project Structure


- `data/`: Contains the dataset used for analysis.

- `notebooks/`: Jupyter notebooks with step-by-step explanations of the data processing, clustering, and model development.

- `images/`: This folder contains images used in the project, such as diagrams or visualizations, that might be included in the documentation or displayed on the web app.

- `myenv/`: Another environment folder that might have been used for setting up a different virtual environment. Ensure to use only one virtual environment for consistency.

- `templates/`: Contains the HTML templates for the Flask web application. These templates define the structure and layout of the web pages.

- `.gitignore`: A file that specifies which files and directories Git should ignore. Commonly used to exclude environment folders, compiled code, and other unnecessary files from being tracked by Git.

- `README.md`: The main documentation file for the project, providing an overview, instructions, and other essential information.

- `app.py`: The main Python script that runs the Flask web application. This file includes the route definitions, model loading, and request handling logic.

- `model.pkl`: The serialized machine learning model file. It is loaded in `app.py` to make predictions based on user input.

## Installation and Usage
1. Clone the repository:
   git clone (https://github.com/Sujal3141/Customer-Segmentation-Analysis-.git)
2. Create a virtual environment and activate it:
  `myenv\Scripts\activate`
3. Install the required packages:
   pip install -r requirements.txt
4. Run the Flask application:
    python app.py
5. Access the web application:
    Open the generated link in the terminal .
   
You can access the live web application for customer segmentation analysis at the following link:
[Customer Segmentation Analysis Web App](https://customer-segmentation-analysis.onrender.com/)
