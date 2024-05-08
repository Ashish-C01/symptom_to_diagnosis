# Disease diagnosis using symptom [Application](https://huggingface.co/spaces/ashish-001/Symptoms_2_Diagnosis)
Web application to classify disease  based on short description of symptom.



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
