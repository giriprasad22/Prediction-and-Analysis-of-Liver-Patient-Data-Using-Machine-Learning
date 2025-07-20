# Prediction-and-Analysis-of-Liver-Patient-Data-Using-Machine-Learning

A machine learning system for predicting liver disease risk from patient data, featuring:

- Data analysis and visualization
- Predictive modeling (using `.h5` and `.pkl` models)
- Flask-based web interface

## 📁 Project Structure
.
├── app.py # Flask application entry point

├── project.ipynb # Jupyter Notebook with EDA and modeling

├── indian_liver_patient.csv # Original dataset

├── liver.h5 # Trained Keras/TensorFlow model

├── liver_analysis.pkl # Serialized analysis/model object

├── static/

│ └── css/ # Stylesheets

├── templates/ # HTML templates

└── README.md # Documentation


## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### 1. Clone the repository
bash

git clone https://github.com/giriprasad22/Prediction-and-Analysis-of-Liver-Patient-Data-Using-Machine-Learning.git

cd Prediction-and-Analysis-of-Liver-Patient-Data-Using-Machine-Learning

## 2 Install dependencies

bash

pip install -r requirements.txt

(Note: If requirements.txt is missing, install these manually:)

bash

pip install flask pandas numpy scikit-learn tensorflow matplotlib

## 3 Run the application

bash

python app.py

The web interface will launch at http://localhost:5000

### 🔍 Understanding the Components

## Data Files

indian_liver_patient.csv: Original dataset from Kaggle

liver.h5: Pretrained Keras model (TensorFlow backend)

liver_analysis.pkl: Serialized scikit-learn model/analysis object

## Code Files

project.ipynb: Contains complete EDA, feature engineering, and model training

app.py: Flask web application with these routes:

/: Homepage with data input form

/predict: Prediction endpoint

/analysis: Data visualization dashboard

## 🛠️ Development Workflow

1 Data Exploration:

Open project.ipynb in Jupyter Notebook

Contains all data preprocessing steps

2 Model Training:

Notebook includes model training code

Outputs saved as liver.h5 (Keras) and liver_analysis.pkl

3 Web Interface:

Customize templates in /templates

Modify styles in /static/css

## 📊 Sample Output

After running app.py, you should see:

Interactive input form at homepage

Prediction results page with risk probability

Analysis dashboard with visualizations

## 🤝 Contributing

Contributions welcome! Please:

Fork the repository

Create a feature branch

Submit a pull request
