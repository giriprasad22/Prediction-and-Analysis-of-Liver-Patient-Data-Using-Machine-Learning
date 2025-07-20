from flask import Flask, render_template, request
import pickle
import joblib

import numpy as np
from tensorflow.keras.models import load_model

ct = joblib.load("liver")
sc = pickle.load(open("liver_analysis.pkl","rb"))
model = load_model("liver.h5")

app = Flask(__name__)
@app.route('/')
def loadpage():
    return render_template("index.html")

@app.route('/y_predict', methods = ["POST"])
def prediction():
    Gender = request.form["Gender"]
    Age = request.form["Age"]
    Total_Bilirubin = request.form["Total_Bilirubin"]
    Direct_Bilirubin = request.form["Direct_Bilirubin"]
    Alkaline_Phosphotase = request.form["Alkaline_Phosphotase"]
    Alamine_Aminotransferase = request.form["Alamine_Aminotransferase"]
    Aspartate_Aminotransferase = request.form["Aspartate_Aminotransferase"]
    Total_Protiens = request.form["Total_Protiens"]
    Albumin = request.form["Albumin"]
    Albumin_and_Globulin_Ratio = request.form["Albumin_and_Globulin_Ratio"]
    
    
    data = [[Gender,float(Age),float(Total_Bilirubin),float(Direct_Bilirubin),float(Alkaline_Phosphotase),float(Alamine_Aminotransferase),float(Aspartate_Aminotransferase),float(Total_Protiens),float(Albumin),float(Albumin_and_Globulin_Ratio)]]
    p = np.array(sc.transform(ct.transform(data)))
    p = p.astype(np.float32)

    
    prediction = model.predict(p)[0]
    
    if(prediction == 1):
        return render_template("index.html",prediction_text = "You have a liver disease problem , you must go to doctor" )
    else:
        return render_template("index.html",prediction_text = "You dont have a liver disease problem" )
    
if __name__ == "__main__":
    app.run(debug = True)
