# 📊 Telco Customer Churn Prediction

## 🚀 Overview

This project aims to predict customer churn and identify the key drivers behind it using machine learning and model explainability techniques.

Beyond prediction, the focus is on **understanding why customers churn** and how businesses can act on those insights.

---

## 🎯 Objective

* Predict whether a customer will churn
* Minimize missed churn cases (false negatives)
* Extract actionable insights for retention strategies

---

## 🧠 Methodology

### 1. Data Preparation

* Cleaned missing values (`TotalCharges`)
* Encoded categorical variables
* Stratified train-test split

---

### 2. Models

#### Logistic Regression

* Strong baseline
* ROC-AUC ≈ 0.83
* Limited recall (~0.57)

---

#### Decision Tree

* Captured non-linear relationships
* Improved recall (~0.61)
* Sensitive to overfitting

---

#### XGBoost (Final Model)

* Gradient boosting with regularization
* Handled class imbalance (`scale_pos_weight`)
* Tuned using RandomizedSearchCV

---

## ⚙️ Model Optimization

* Cross-validation (StratifiedKFold)
* Hyperparameter tuning
* Threshold tuning to control recall vs precision

> Key insight: Model performance depends not only on training, but also on how predictions are converted into decisions.

---

## 📈 Final Results

* **ROC-AUC:** ~0.84
* **Recall (Churn):** ~0.78
* **False Negatives reduced significantly vs baseline**

Trade-off:

* Higher recall increases false positives, which may increase operational cost

---

## 🔍 Model Explainability (SHAP)

SHAP was used to interpret predictions and identify churn drivers.

### Key Insights:

* 📉 **Low tenure** → strongly increases churn risk
* 📄 **Month-to-month contracts** → high churn probability
* 💰 **High monthly charges** → increased churn likelihood
* 🛠️ Additional services → reduce churn probability

---

### SHAP Summary Plot

![SHAP Summary](images/shap_summary.png)

---

## 💡 Business Insights

* Focus retention efforts on **new customers**
* Encourage **long-term contracts**
* Monitor customers with **high monthly charges**
* Promote value-added services to reduce churn

---

## 🧩 Key Learnings

* Class imbalance significantly impacts model behavior
* Threshold tuning is critical in classification problems
* Model interpretability is essential for business adoption

---

## 🔮 Future Improvements

* Compare with resampling techniques (SMOTE)
* Deploy model as an API
* Build a dashboard for real-time insights

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* XGBoost
* SHAP
* Pandas / NumPy

---

## 📬 Contact

If you’d like to discuss this project or collaborate, feel free to reach out.
