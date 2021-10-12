# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'dt_grid_model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('new.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        name1 = str(request.form['name1'])
        rest_ecg_2 = 0
        slope_2 = 0
        ca_1 = 0
        ca_2 = 0
        ca_3 = 0
        ca_4 = 0

        chest_pain_1=0
        chest_pain_2=0
        chest_pain_3=0

        thalassemia_1 = 0
        thalassemia_2 = 0
        thalassemia_3 = 0

        gender_1 = int(request.form['gender'])

        age = int(request.form['age'])
        rest_bps = int(request.form['bp'])
        cholestrol = int(request.form['chl'])
        thalach = int(request.form['hrate'])
        old_peak = int(request.form['oldpeak'])

        fasting_blood_sugar_1 = int(request.form['bloodsugar'])
        rest_ecg_1 = int(request.form['klevel'])
        if (rest_ecg_1 == 1):
            rest_ecg_1 = 1
            rest_ecg_2 = 0
        elif (rest_ecg_1 == 2):
            rest_ecg_1 = 0
            rest_ecg_2 = 1

        exer_angina_1 = int(request.form['exer'])

        slope_1 = int(request.form['slope'])
        if (slope_1 == 1):
            slope_1 = 1
            slope_2 = 0
        elif (slope_1 == 2):
            slope_1 = 0
            slope_2 = 1
        else:
            slope_1 = 0
            slope_2 = 0

        ca = int(request.form['action'])
        if (ca == 1):
            ca_1 = 1
        elif (ca == 2):
            ca_2 = 1
        elif (ca == 3):
            ca_3 = 1
        elif (ca == 4):
            ca_4 = 1

        thalassemia = int(request.form['action1'])
        if (thalassemia == 1):
            thalassemia_1 = 1
        elif (thalassemia == 2):
            thalassemia_2 = 1
        elif (thalassemia == 3):
            thalassemia_3 = 1

        chest_pain = int(request.form['action1'])
        if (chest_pain == 1):
            chest_pain_1 = 1
        elif (chest_pain == 2):
            chest_pain_2 = 1
        elif (chest_pain == 3):
            chest_pain_3 = 1

        data = np.array([[age, rest_bps, cholestrol, thalach, old_peak, gender_1,chest_pain_1, chest_pain_2, chest_pain_3, fasting_blood_sugar_1,rest_ecg_1, rest_ecg_2, exer_angina_1, slope_1, slope_2,ca_1, ca_2, ca_3, ca_4, thalassemia_1, thalassemia_2,thalassemia_3]])

        my_prediction = classifier.predict(data)

        return render_template('HeartDiseaseResult.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)