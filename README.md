# sentimental-analysis-NLP
An NLP-based sentiment analysis project built with Python, Scikit-learn, CountVectorizer, and Multinomial Naive Bayes. Features text preprocessing, machine learning model training, evaluation, and a Streamlit web app for real-time sentiment prediction.
# Sentiment Analysis using NLP and Machine Learning

## 📌 Project Overview

This project is a **Sentiment Analysis** application built using **Natural Language Processing (NLP)** and **Machine Learning**. It analyzes text input and predicts the corresponding sentiment/emotion based on the trained model. The project demonstrates the complete NLP workflow, including text preprocessing, feature extraction, model training, evaluation, and deployment through a user-friendly Streamlit interface.

## 🚀 Features

* Text preprocessing (lowercasing, punctuation removal, stopword removal, etc.)
* Feature extraction using **CountVectorizer (Bag of Words)**
* Sentiment/Emotion prediction using **Multinomial Naive Bayes**
* Model evaluation with accuracy and classification metrics
* Interactive **Streamlit** web application
* Fast and lightweight prediction system

## 🛠️ Technologies Used

* Python
* Natural Language Processing (NLP)
* Pandas
* NumPy
* Scikit-learn
* CountVectorizer (Bag of Words)
* Multinomial Naive Bayes
* Streamlit
* Pickle

## 📂 Project Workflow

1. Load and preprocess the dataset.
2. Split the dataset into training and testing sets.
3. Convert text into numerical features using **CountVectorizer**.
4. Train a **Multinomial Naive Bayes** classifier.
5. Evaluate the model using accuracy and classification reports.
6. Save the trained model and vectorizer.
7. Deploy the model with a **Streamlit** web application for real-time predictions.

## 📊 Model

* **Algorithm:** Multinomial Naive Bayes
* **Feature Extraction:** Bag of Words (CountVectorizer)
* **Evaluation Metrics:** Accuracy, Precision, Recall, and F1-Score

## 📷 Application

Users can enter any text into the Streamlit interface, and the model predicts the corresponding sentiment/emotion along with the confidence score (if enabled).

## 📁 Project Structure

```text
Sentiment-Analysis/
│── app.py
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
│── README.md
│── notebook.ipynb
```

## ▶️ How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application

```bash
streamlit run app.py
```

## 🎯 Future Improvements

* Use TF-IDF and compare performance.
* Train advanced models such as Logistic Regression, SVM, and Random Forest.
* Experiment with deep learning models like LSTM or BERT.
* Deploy the application on Streamlit Community Cloud.
* Add confidence visualization and probability charts.

## 📄 License

This project is intended for educational and learning purposes.
