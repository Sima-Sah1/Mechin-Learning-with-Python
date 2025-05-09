
import streamlit as st
import joblib 
import re
import nltk

# NLTK imports

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

#Load Resources
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
model = joblib.load('nb_model.pkl')

#Page configuration
st.set_page_config(page_title="News Categorization",page_icon="👩‍💻",layout="centered")


st.title("NEWS CATEGORIZATION !")
st.markdown("Enter a news headline or article below.")
st.markdown('---')
input_text = st.text_area("Enter News Text:",height=200)

#Text Preprocessing Function

def preprocess_text(text):
    #Lowercasing
    text = text.lower()
    # Remove special characters and punctation
    text = re.sub(r'[^a-zA-Z\s]','',text)
    # Totenization
    words = word_tokenize(text)
    #Remove stopwords and lemmatize
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    # Join back into a string
    return " ".join(words)

# Prediction Function 
def predict_category(text):
    processed_text = preprocess_text(text)
    prediction = model.predict([processed_text])
    return prediction[0]

# Prediction Display 
if st.button("🔍 Predict Category"):
    if input_text.strip():
        category = predict_category(input_text)
        st.success(f'**Predicted Category:**{category}')
    else:
        st.warning("please enter some text first")

#Footer
st.markdown("---")
st.markdown('<p style="text-align:center;">Built by sima sah </p',unsafe_allow_html=True)