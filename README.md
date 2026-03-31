# 📧 Email Spam Classifier

A Machine Learning based **Email/SMS Spam Classifier** built with **Python, Scikit-learn, NLTK, and Streamlit**.  
This project predicts whether a message is **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) techniques.

---

##  Live Demo
👉 Add your deployed app link here:  
[Live App](https://email-spam-classifier-43g5.onrender.com)

---

##  Features

- Classifies messages as **Spam** or **Not Spam**
- Clean and interactive **Streamlit UI**
- Text preprocessing using **NLP**
- Uses **TF-IDF Vectorization**
- Machine Learning model for accurate prediction
- Easy to deploy and use

---

##  Machine Learning Workflow

The project follows this pipeline:

1. **Text Input**
2. **Text Preprocessing**
   - Lowercasing
   - Tokenization
   - Removing special characters
   - Removing stopwords
   - Stemming
3. **Vectorization**
   - TF-IDF Transformer
4. **Prediction**
   - Spam / Not Spam

---

##  Tech Stack

### **Frontend**
- Streamlit

### **Backend / ML**
- Python
- Scikit-learn
- NLTK
- Pickle

### **Deployment**
- Render / Streamlit Cloud / Heroku

---

##  Project Structure

```bash
email-spam-classifier/
│── main.py
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
│── setup.sh
│── README.md
