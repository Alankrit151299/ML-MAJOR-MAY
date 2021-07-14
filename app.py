import streamlit as st
import joblib
st.title('Sentiment Analysis Deployment')
test_model = joblib.load('Sentiment_Analysis')
ip = st.text_input('Enter your message')
op = test_model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
