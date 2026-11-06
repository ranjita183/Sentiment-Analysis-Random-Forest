# 🛒 Amazon Review Sentiment Analysis using Random Forest

A Machine Learning and Natural Language Processing (NLP) project that classifies Amazon product reviews as **Positive** or **Negative** using the **Random Forest Classifier** and **CountVectorizer**.

---

## 📌 Project Overview

Customer reviews contain valuable insights about products. This project applies Natural Language Processing (NLP) techniques to convert text reviews into numerical features and trains a Random Forest model to automatically predict the sentiment of a review.

---

## 🎯 Features

- Text Preprocessing using CountVectorizer
- Sentiment Label Encoding
- Train-Test Split
- Random Forest Classification
- Sentiment Prediction
- Model Evaluation using Accuracy Score
- Classification Report

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- CountVectorizer
- Random Forest Classifier

---

## 📂 Dataset

The dataset contains two columns:

| Feature | Description |
|---------|-------------|
| Review | Customer review text |
| Sentiment | Positive or Negative |

---

## 📁 Project Structure

```
Amazon-Review-Sentiment-Analysis
│
├── dataset
│   └── amazon_reviews_100_mixed.csv
│
├── source
│   └── sentiment_analysis.py
│
├── images
│   └── workflow.png
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Amazon-Review-Sentiment-Analysis.git
```

### Navigate to the project folder

```bash
cd Amazon-Review-Sentiment-Analysis
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python sentiment_analysis.py
```

---

## 🔄 Machine Learning Workflow

```
Customer Reviews
       │
       ▼
Text Vectorization
(CountVectorizer)
       │
       ▼
Feature Extraction
       │
       ▼
Train-Test Split
       │
       ▼
Random Forest Classifier
       │
       ▼
Sentiment Prediction
       │
       ▼
Model Evaluation
```

---

## 💬 Example Prediction

**Input Review**

```
Met expectations
```

**Predicted Output**

```
Positive 😊
```

---

## 📊 Evaluation Metrics

- Accuracy Score
- Precision
- Recall
- F1-Score
- Classification Report

---

## 🚀 Future Improvements

- Use TF-IDF Vectorizer for better feature representation.
- Experiment with Logistic Regression, Naive Bayes, and Support Vector Machine (SVM).
- Apply text preprocessing techniques such as stop-word removal and stemming.
- Train on a larger dataset to improve accuracy.
- Build a web application using Streamlit or Flask for real-time sentiment prediction.

---

## 📚 Libraries Used

- Pandas
- Scikit-learn

Install all required packages using:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

**Shivanand Hanchinal**

Electronics & Communication Engineering Student

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.# Sentiment-Analysis-Random-Forest
