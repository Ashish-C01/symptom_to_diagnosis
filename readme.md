# Disease diagnosis using symptom [Application](https://huggingface.co/spaces/ashish-001/Symptoms_2_Diagnosis)
Web application to classify disease  based on short description of symptom.
This project leverages a fine-tuned BERT model to classify diseases based on user-provided symptoms. The model is trained on a dataset covering 24 different diseases, enabling it to provide accurate and efficient diagnoses. The project encompasses data preprocessing, model training, and evaluation.

### Key Features
- **BERT Model**: Utilizes a pre-trained BERT model fine-tuned for disease classification.
- **Comprehensive Dataset**: Covers 24 diseases, including Psoriasis, Varicose Veins, Typhoid, Chickenpox, and more.
- **Accurate Diagnosis**: Provides precise disease predictions based on user symptoms.

### Diseases Covered
- Psoriasis
- Varicose Veins
- Typhoid
- Chickenpox
- Impetigo
- Dengue
- Fungal Infection
- Common Cold
- Pneumonia
- Dimorphic Hemorrhoids
- Arthritis
- Acne
- Bronchial Asthma
- Hypertension
- Migraine
- Cervical Spondylosis
- Jaundice
- Malaria
- Urinary Tract Infection
- Allergy
- Gastroesophageal Reflux Disease
- Drug Reaction
- Peptic Ulcer Disease
- Diabetes

### Result on test data
![Result](<Result.png>)

## Steps to run the program on Windows
1. Create a virtual environment 
```
python -m venv "environment name"
```
2. Activate the virtual environment
```
"environment name"\Scripts\activate
```
3. Install all required libraries
```
pip install -r requirements.txt
```
4. Download the model from the [link](https://huggingface.co/ashish-001/finetuned-bert-symptom/resolve/main/symptoms.h5?download=true) and paste it in the same directory

5. Run the program
```
streamlit run app.py
```

## Images
![Alt text](<demo.gif>)
