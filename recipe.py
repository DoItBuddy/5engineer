import os
import google.generativeai as genai
import streamlit as st 

st.title('Recipe Generator')


os.environ['GOOGLE_API_KEY'] = "AIzaSyDKZfrp8nBSHOWizR4Dz2xSMEC4lvO3D04"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


ingredients = st.text_area("Enter Ingredients (comma-separated)", "e.g., chicken, garlic, onions, tomatoes")
dish = st.text_input("What would you like to make?", "e.g., curry, soup, pasta")


model = genai.GenerativeModel('gemini-pro')


if st.button('Generate Recipe'):
    prompt = f"""
    You are a professional chef with expertise in creating recipes.
    Help me create a recipe for the following dish using the provided ingredients:
    
    Dish: {dish}
    Ingredients: {ingredients}
    
    Please provide step-by-step instructions for preparing the dish.
    """
    response = model.generate_content(prompt)
    st.subheader("Generated Recipe:")
    st.success(response.text)
