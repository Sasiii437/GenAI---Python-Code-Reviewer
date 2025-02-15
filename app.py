import streamlit as st
import google.generativeai as ai
from dotenv import load_dotenv

load_dotenv()
import os
api_key = st.secrets["general"]["API_KEY"]
ai.configure(api_key=API_KEY)

sys_prompt = """ You are a great Python code reviewer and you work is to review the user input python code and you want to find the bugs in it and want to generate the bug report and also to give the explanation of corrected code. You have to provide the information without any grammar mistakes.
                You have to give the code by fixing the errors to the user and its explanation . Don't miss the explanation too and usecases of the corrected code in Python. First give Bug Report and after that corrected code. Give the side headings in Bold and size should be greater than normal text, like thrice the size of normal text .
                If the user provides queries which are irrelevently to Python or Python code, then you have kindly inform the user that you are designed for what purposes and your capability in which work and it should be in interactive. 
            """

gemini_model = ai.GenerativeModel(model_name="models/gemini-1.5-pro",system_instruction=sys_prompt)

st.title("AI Python Code Reviewer")
user_input=st.text_area(label="Enter your Python code here" , placeholder="Enter your Python code for reviewing ")
bt_click=st.button("Generate")

if bt_click == True:
    response=gemini_model.generate_content(user_input)
    print("OUTPUT on terminal : ",len(response.text))
    st.write(response.text)
