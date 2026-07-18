Check here: 
https://churnpredictionusingneuralnetworksclassification.streamlit.app/

------------------------------------------------------
# Customer Churn Prediction Using Neural Networks

## 📌 Project Overview

Customer churn prediction is a critical business problem where companies identify customers who are likely to discontinue their services. This project uses an **Artificial Neural Network (ANN)** built with **TensorFlow/Keras** to predict customer churn based on demographic and banking information.

The trained model is deployed as an interactive web application using **Streamlit**, allowing users to input customer details and receive real-time churn predictions.

---

## 🎯 Problem Statement

Banks lose significant revenue when customers leave their services. Predicting customer churn enables organizations to:

- Retain valuable customers
- Improve customer satisfaction
- Design targeted marketing campaigns
- Reduce customer acquisition costs

This project aims to classify whether a customer is likely to **Exit (Churn)** or **Stay**.

---

## 📂 Dataset

The project uses the **Churn_Modelling.csv** dataset containing customer information such as:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card
- Is Active Member
- Estimated Salary

### Target Variable

- **Exited**
  - **0** → Customer Stays
  - **1** → Customer Churns

---

## 🧠 Model Architecture

The model is built using TensorFlow/Keras.

**Architecture**

- Input Layer
- Hidden Dense Layer (ReLU)
- Hidden Dense Layer (ReLU)
- Output Layer (Sigmoid)

**Training Configuration**

- Optimizer: Adam
- Loss Function: Binary Crossentropy
- Evaluation Metric: Accuracy

---

## ⚙️ Project Workflow

```
Dataset
    │
    ▼
Data Preprocessing
    │
    ▼
Label Encoding
    │
    ▼
One-Hot Encoding
    │
    ▼
Feature Scaling
    │
    ▼
Train ANN Model
    │
    ▼
Save Model & Encoders
    │
    ▼
Deploy with Streamlit
```

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- Scikit-learn
- Pandas
- NumPy
- Streamlit
- Matplotlib
- TensorBoard

---

## 📁 Project Structure

```
ChurnPrediction_UsingNeuralNetworks_Classification/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── model.h5
├── scaler.pkl
├── label_encoder.pkl
├── onehot_encoder.pkl
├── Churn_Modelling.csv
├── experiments.ipynb
├── prediction.ipynb
├── logs/
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/adyant28-main/ChurnPrediction_UsingNeuralNetworks_Classification.git
```

Navigate to the project

```bash
cd ChurnPrediction_UsingNeuralNetworks_Classification
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 💻 Streamlit Application

The application allows users to:

- Select Geography
- Select Gender
- Enter Credit Score
- Enter Age
- Enter Balance
- Enter Number of Products
- Enter Estimated Salary
- Predict Customer Churn

The application outputs:

- Churn Probability
- Final Prediction (Stay or Exit)

---

## 📊 Machine Learning Pipeline

✔ Data Cleaning

✔ Feature Engineering

✔ Label Encoding

✔ One-Hot Encoding

✔ Standard Scaling

✔ Neural Network Training

✔ Model Serialization

✔ Web Application Deployment

---

## 📈 Model Files

The trained model and preprocessing objects are saved as:

- `model.h5`
- `scaler.pkl`
- `label_encoder.pkl`
- `onehot_encoder.pkl`

These files are loaded directly by the Streamlit application for making predictions.

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```
images/
    home.png
    prediction.png
```

Then include them in the README:

```markdown
![Home Page](images/home.png)

![Prediction](images/prediction.png)
```

---

## 🔮 Future Improvements

- Hyperparameter tuning
- Cross-validation
- Explainable AI using SHAP
- Docker deployment
- REST API using FastAPI
- CI/CD pipeline
- Cloud deployment
- Model monitoring

---

## 📚 Learning Outcomes

This project demonstrates:

- Deep Learning for Binary Classification
- Data Preprocessing
- Feature Engineering
- TensorFlow/Keras
- Model Deployment
- Streamlit Application Development
- Git & GitHub Workflow

---

## 👨‍💻 Author

**Adyant**

GitHub: https://github.com/adyant28-main

---

## ⭐ If you found this project useful

Give this repository a ⭐ on GitHub!
