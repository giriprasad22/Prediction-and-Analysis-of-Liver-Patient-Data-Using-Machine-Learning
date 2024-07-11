from flask import Flask, render_template, request
import pickle
import numpy as np

sc = pickle.load(open('sc.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

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
    
    
    data = [[float(Gender),float(Age),float(Total_Bilirubin),float(Direct_Bilirubin),float(Alkaline_Phosphotase),float(Alamine_Aminotransferase),float(Aspartate_Aminotransferase),float(Total_Protiens),float(Albumin),float(Albumin_and_Globulin_Ratio)]]
    
    data = sc.transform(data)
    
    prediction = model.predict(data)
    
    if(prediction > 0.5):
        return render_template("index.html",prediction_text = "You have a liver disease problem , you must go to doctor" )
    else:
        return render_template("index.html",prediction_text = "You dont have a liver disease problem" )
    
if __name__ == "__main__":
    app.run(debug = True)
