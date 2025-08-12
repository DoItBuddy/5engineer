import os
import google.generativeai as genai
import streamlit as st 
st.title('Sentiment Analysis')

os.environ['GOOGLE_API_KEY'] = "AIzaSyDKZfrp8nBSHOWizR4Dz2xSMEC4lvO3D04"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

user_input = st.text_area("Enter your Review", 'Review')
model = genai.GenerativeModel('gemini-pro')

if(st.button('Answer')):
    prompt = f"""
    you ae an expert linguist , who is good at classifing customer review sentiments into positive/negative label
    help me classify customer reviews into: positive(positive review), and negative (negative review).
    
    '''
    {user_input}
    '''
    """
    response = model.generate_content(prompt)
    st.success("{}.".format(response.text))