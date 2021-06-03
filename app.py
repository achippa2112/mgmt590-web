import requests
import json
import streamlit as st
import os

url = "{}".format(os.environ.get('PG_API_URL'))
st.title('Amazing Question Answering Thing!')

# Inputs
question = st.text_input('Question')
context = st.text_area('Context')

# Execute question answering on button press
if st.button('Answer Question'):

    payload = json.dumps({
        "question": question,
        "context": context
        })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url+"/answer", headers=headers, data=payload)
    answer = response.json()['answer']

    st.success(answer)
