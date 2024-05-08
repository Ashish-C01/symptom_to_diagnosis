import tensorflow as tf
import streamlit as st
import transformers
import numpy as np
import pickle
import string

model = tf.keras.models.load_model('symptoms.h5', custom_objects={
                                   "TFBertModel": transformers.TFBertModel})
with open('tokenizer.pkl', 'rb') as f:
    pickled_data = pickle.load(f)
    tokenizer = pickled_data['tokenizer']
    label_encoder = pickled_data['label_encoder']


def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


st.set_page_config(page_title="Symptom 2 Diagnosis")
st.title('Symptom 2 Diagnosis')
symptom = st.text_area('Enter the symptom')
if st.button("Diagnose"):
    symptom = symptom.strip()
    if symptom != '':
        preprocess_symptom = preprocess_text(symptom)
        data = tokenizer(
            text=preprocess_symptom,
            add_special_tokens=True,
            max_length=55,
            truncation=True,
            padding='max_length',
            return_tensors='tf',
            return_token_type_ids=False,
            return_attention_mask=True,
            verbose=True
        )
        prediction = model.predict(
            {'input_ids': data['input_ids'], 'attention_mask': data['attention_mask']})
        class_index = np.argmax(prediction)
        st.write(
            f'Diagnosed as {label_encoder.inverse_transform([class_index])[0]}')
    else:
        st.write('Please enter the symptom')
