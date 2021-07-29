#core plugins
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import joblib
#fxn
pipe_lr=joblib.load(open("models/emotion_classifier_pipeline_logistic_july_28.pkl"))
def predict_emotions(docx):
    result =pipe_lr.predict([docx])
    return results[0]
def get_prediction_proba(docx):
    results=pipe_lr.predict_proba([docx])
    return results







def main():
    st.title('Emotion Classifier App')
    menu=['Home','Monitor','About']
    choise=st.sidebar.selectbox('Menu',menu)

    if choise=='Home':
        st.subheader('Home-Emotion In Text')
        with st.form(key='emotion_clf_form'):
         raw_text=st.text_area('Type Here')
         submit_text=st.form_submit_button(label='Submit')
        if submit_text:
            col1,col2=st.beta_column(2)
            prediction=predict_emotions(raw_text)
            probability=get_prediction_proba(raw_text)
            with col1:
                st.success("original text")
                st.write(raw_text)
                st.success('prediction')
            with col2:
                st.success('prediction probability')


    elif choise=='Monitor':
        st.subheader('Monıtor App')

    elif choise=='About':
        st.subheader('About')
