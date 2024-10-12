# breast-cancer-logistic-regression
 This repository demonstrates the use of Logistic Regression to classify breast cancer tumors as benign or malignant using the Breast Cancer Wisconsin (Original) dataset. It includes data exploration, model building with both full and subset feature sets, and performance evaluation using cross-validation.
 
# Breast Cancer Classification using Logistic Regression

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview
This project demonstrates how to use **Logistic Regression** to classify breast cancer tumors as either **benign** or **malignant** using the **Breast Cancer Wisconsin (Original)** dataset. The dataset consists of features derived from cell nuclei measurements that can be used to predict the nature of breast tumors. The model is built using Python's `scikit-learn` library.

## Dataset
The dataset used in this project is the **Breast Cancer Wisconsin (Original)** dataset, made publicly available through the UCI Machine Learning Repository:

**Citation**:  
Wolberg, W. (1990). *Breast Cancer Wisconsin (Original) [Dataset]*. UCI Machine Learning Repository. [https://doi.org/10.24432/C5HP4Z](https://doi.org/10.24432/C5HP4Z)

### Features:
- **Clump Thickness**
- **Uniformity of Cell Size**
- **Uniformity of Cell Shape**
- **Marginal Adhesion**
- **Bare Nuclei**
- **Bland Chromatin**
- **Mitoses**
- and more.

### Target:
- **2** - Benign
- **4** - Malignant

## Project Structure
The project is organized as follows:

```plaintext
├── README.md              # Project Overview
├── breast_cancer.csv      # Dataset file
├── Breast Cancer.ipynb    # Jupyter notebook with analysis and model
└── requirements.txt       # Python dependencies
#Objective
The goal of this project is to create a logistic regression model that accurately classifies tumors as benign or malignant. We explore both a model using all features and a model using a subset of key features for comparison.

#Key Steps:
Exploratory Data Analysis (EDA): We analyze the dataset, visualize relationships, and explore the distributions of features.
Feature Engineering: Feature selection based on correlation with the target class.
Model Training: Build logistic regression models using both the full feature set and a subset of important features.
Model Evaluation: Use cross-validation and confusion matrix to assess the performance, accuracy, and consistency of the models.

#Results
* We achieved the following results:

#Subset Model:

* Accuracy: 95.62%
* Cross-Validation Standard Deviation: 2.60%
#All Features Model:

* Accuracy: 96.70%
* Cross-Validation Standard Deviation: 1.97%
* The subset model performs almost as well as the full model while being simpler and more interpretable.

Dependencies
To run this project, install the required Python packages using:


numpy
pandas
matplotlib
seaborn
scikit-learn

#References
Wolberg, W. (1990). Breast Cancer Wisconsin (Original) [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5HP4Z
