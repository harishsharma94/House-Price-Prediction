# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project is a Machine Learning-based House Price Prediction application.

The objective is to build a complete end-to-end Machine Learning workflow that takes historical house data, performs exploratory data analysis and preprocessing, trains and compares multiple regression models, selects the best-performing model, and deploys the final model through a Streamlit web application.

The application allows a user to enter house characteristics such as number of bedrooms, bathrooms, living area, lot area, location, and other property details and receive an estimated house price.

---

## 🎯 Objective

The main objectives of this project are:

- Understand and explore a real-world house price dataset.
- Perform Exploratory Data Analysis (EDA).
- Identify relevant features for predicting house prices.
- Handle missing values and categorical variables.
- Apply appropriate feature preprocessing.
- Train multiple Machine Learning regression models.
- Compare model performance using evaluation metrics.
- Select the best-performing model.
- Create a reusable Machine Learning pipeline.
- Save the trained pipeline for future predictions.
- Build and deploy a user-friendly Streamlit application.

---

## 📊 Dataset

The project uses a house price dataset containing information about residential properties.

The dataset includes features such as:

- `bedrooms` – Number of bedrooms
- `bathrooms` – Number of bathrooms
- `sqft_living` – Living area in square feet
- `sqft_lot` – Lot area in square feet
- `floors` – Number of floors
- `waterfront` – Whether the property has a waterfront
- `view` – View rating
- `condition` – Property condition
- `sqft_above` – Above-ground living area
- `sqft_basement` – Basement area
- `yr_built` – Year the house was built
- `yr_renovated` – Year the house was renovated
- `street` – Street address
- `city` – City
- `statezip` – State and ZIP code
- `price` – Target variable

The target variable for this project is:

`price`

---

## 🔎 Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed before building the Machine Learning models.

The analysis included:

- Understanding the structure of the dataset.
- Checking data types.
- Identifying missing values.
- Examining numerical features.
- Examining categorical features.
- Understanding the distribution of house prices.
- Analyzing relationships between important features and house prices.
- Identifying potential outliers.
- Evaluating correlations between numerical variables.

EDA was used to help determine which features should be retained, transformed, or removed before model training.

---

## 🧩 Features Used

### Numerical Features

The following numerical features were used:

- `bedrooms`
- `bathrooms`
- `sqft_living`
- `sqft_lot`
- `floors`
- `waterfront`
- `view`
- `condition`
- `sqft_above`
- `sqft_basement`
- `yr_built`
- `yr_renovated`

### Categorical Features

The following categorical features were used:

- `city`
- `statezip`

The following columns were excluded from the model:

- `date`
- `price` – target variable
- `country`
- 'street'

---

## ⚙️ Data Preprocessing

The dataset contains both numerical and categorical features, so different preprocessing techniques were applied.

### Numerical Features

For numerical features:

1. Missing values were handled using `SimpleImputer`.
2. Features were standardized using `StandardScaler`.

The preprocessing was implemented using a Scikit-learn `Pipeline`.

### Categorical Features

Categorical features were transformed using:

`OneHotEncoder`

with:

`handle_unknown='ignore'`

This allows the model to handle previously unseen categorical values during prediction.

### ColumnTransformer

A `ColumnTransformer` was used to apply the appropriate preprocessing to numerical and categorical features.

The overall preprocessing structure is:

```text
Numerical Features
       ↓
SimpleImputer
       ↓
StandardScaler
       ↓
Processed Numerical Features

Categorical Features
       ↓
OneHotEncoder
       ↓
Processed Categorical Features

🤖 Models Compared

Three regression models were evaluated:

1. Linear Regression

A simple baseline regression model used to establish a starting point for performance.

2. Random Forest Regressor

An ensemble model that combines multiple decision trees to improve prediction performance and reduce overfitting.

3. Gradient Boosting Regressor

An ensemble technique that builds models sequentially, with each new model attempting to improve the errors made by previous models.

📈 Model Evaluation

The models were evaluated using the following metrics:

Mean Absolute Error (MAE)

Measures the average absolute difference between the actual and predicted house prices.

Lower MAE is better.

Root Mean Squared Error (RMSE)

Measures prediction error while giving greater weight to larger errors.

Lower RMSE is better.

R² Score

Measures how much of the variation in house prices is explained by the model.

Higher R² is better.

The models were compared using these metrics, and the best-performing model was selected based on the overall results.

🏆 Best Model

After comparing the models, Linear Regression was selected as the final model based on the evaluation results obtained during model comparison.

The final model was integrated with the preprocessing steps into a single Machine Learning pipeline.

The pipeline contains:

Input Data
    ↓
SimpleImputer
    ↓
StandardScaler / OneHotEncoder
    ↓
Linear Regression
    ↓
Predicted House Price
💾 Model Pipeline

The complete preprocessing and Machine Learning model were saved as a single pipeline using joblib.

The saved model is located at:

models/house_price_pipeline.pkl

Saving the complete pipeline ensures that the same preprocessing applied during model training is automatically applied when making predictions on new data.

🌐 Streamlit Application

A Streamlit application was created to provide a simple user interface for the trained Machine Learning model.

The user can enter information such as:

Bedrooms
Bathrooms
Living area
Lot area
Floors
Waterfront
View
Condition
Basement area
Year built
Year renovated
City
State/ZIP

The application then passes the user input through the saved Machine Learning pipeline and displays the predicted house price.

Application Flow
User Input
    ↓
Streamlit Application
    ↓
Saved ML Pipeline
    ↓
Preprocessing
    ↓
Linear Regression Model
    ↓
Predicted House Price
▶️ How to Run the Application
1. Clone the repository
git clone <your-gitlab-repository-url>
2. Navigate to the project
cd house-price-prediction
3. Install required libraries
pip install -r requirements.txt
4. Run the Streamlit application
streamlit run app/app.py

The application will open in your browser.

📁 Project Structure
house-price-prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── raw/
│       └── house_data.csv
│
├── models/
│   └── house_price_pipeline.pkl
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── src/
│
├── .gitignore
├── requirements.txt
└── README.md
🖥️ Application Screenshots
House Price Prediction Application

Add screenshots of the Streamlit application here.

For example:

![Streamlit Application](screenshots/house_price_app.png)
🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Joblib
Streamlit
Git / GitLab
Jupyter Notebook
🚀 Future Improvements

Potential future improvements include:

Hyperparameter tuning.
Additional Machine Learning models.
Improved feature engineering.
More advanced model evaluation.
Better handling of outliers.
Model explainability.
Cloud deployment.
API-based model serving using FastAPI.
Automated model retraining.
Monitoring model performance after deployment.
👨‍💻 Author

Harish Sharma

Machine Learning Project – House Price Prediction

📌 Key Learning

This project demonstrates an end-to-end Machine Learning workflow:

Data Collection
      ↓
Data Exploration
      ↓
EDA
      ↓
Feature Selection
      ↓
Train/Test Split
      ↓
Data Preprocessing
      ↓
Model Training
      ↓
Model Comparison
      ↓
Model Selection
      ↓
Pipeline Creation
      ↓
Model Evaluation
      ↓
Model Persistence
      ↓
Streamlit Deployment

The project demonstrates how a Machine Learning model can be taken from raw data all the way to a working application.