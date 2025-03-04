# Encryptix-Internship

# Titanic Survival Prediction

## 📌 Overview
This is a Streamlit-based web application that predicts whether a passenger on the Titanic would have survived based on input features such as passenger class, number of siblings/spouses aboard, number of parents/children aboard, gender, and embarkation point.

## 🚀 Features
- User-friendly Streamlit interface.
- Accepts passenger details as input.
- Uses a trained machine learning model to predict survival.
- Provides instant predictions with a single click.

## 🛠️ Installation

### Prerequisites
Ensure you have Python installed along with the required dependencies.

### Steps to Run the App
1. Clone the repository or download the project files.
2. Install the required Python libraries:
   ```bash
   pip install streamlit pandas pickle5 numpy
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 📂 Project Structure
```
/Titanic-Survival-Prediction
│── app.py            # Streamlit application script
│── rf_model.pkl      # Trained machine learning model (ensure this file is in the correct path)
│── README.md         # Project documentation
```

## 🔢 Inputs
- **PassengerId**: Unique identifier for a passenger.
- **Pclass**: Ticket class (1st, 2nd, 3rd).
- **SibSp**: Number of siblings/spouses aboard.
- **Parch**: Number of parents/children aboard.
- **Sex_female / Sex_male**: Gender of the passenger.
- **Embarked_C / Embarked_Q / Embarked_S**: Port of embarkation (Cherbourg, Queenstown, Southampton).

## 🎯 Prediction Output
The model predicts whether the passenger survived or not and displays:
- ✅ **Survived**
- ❌ **Did Not Survive**

## 🏗️ Model Details
- The trained model is loaded from `rf_model.pkl`.
- It takes in numeric features and outputs survival probability.
- The model must be placed in the correct directory for the app to function properly.

## 🤖 Future Enhancements
- Improve prediction accuracy by adding more features.
- Deploy the application online for public access.
- Enhance UI with better interactivity and visuals.

- Weather Survived or not: 0 = No, 1 = Yes

