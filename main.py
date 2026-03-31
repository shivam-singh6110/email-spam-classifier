import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download NLTK resources if not available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# डाउनलोड required NLTK data (runs once, safe to keep)
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

# Load stopwords once (efficient)
stop_words = set(stopwords.words('english'))

# Text preprocessing function
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    # Remove non-alphanumeric
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    # Remove stopwords & punctuation
    text = y[:]
    y.clear()

    for i in text:
        if i not in stop_words and i not in string.punctuation:
            y.append(i)

    # Stemming
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# Load trained models safely
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()


# UI
st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

# Button for prediction
if st.button("Predict"):

    if input_sms.strip() == "":
        st.warning("Please enter a message first.")
    else:
        # 1. Preprocess
        transformed_sms = transform_text(input_sms)

        # 2. Vectorize
        vector_input = tfidf.transform([transformed_sms])

        # 3. Predict
        result = model.predict(vector_input)[0]

        # 4. Display
        if result == 1:
            st.error("Spam")
        else:
            st.success("Not Spam")