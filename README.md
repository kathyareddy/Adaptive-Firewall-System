# Adaptive Firewall System

An intelligent firewall system powered by Machine Learning that classifies URLs as **phishing** or **legitimate**, and dynamically updates **Linux firewall rules** to block malicious sites.


---

## Overview

This project combines **Machine Learning**, **network security**, and **real-time user input** to defend against phishing attacks. It uses a **Random Forest Classifier** trained on a labeled dataset of URLs and integrates with **UFW (Uncomplicated Firewall)** to block IPs associated with phishing sites, all through an intuitive **Streamlit** interface.

---

## Tech Stack

- **Python 3**
- **Scikit-learn** – ML Model
- **Pandas, NumPy** – Data processing
- **Streamlit** – UI
- **UFW** – Linux Firewall

---

## Features

-  URL input via Streamlit UI  
-  Classifies URLs as **Phishing** or **Legitimate** using Random Forest  
-  Retrieves IP of phishing URLs and blocks them using UFW  
-  Displays model accuracy and prediction result  
-  Option to unblock previously blocked IPs  

---

## File Structure

```
Adaptive-Firewall-System/
│
├── phishing_site_detection.ipynb      # ML training notebook
├── phishing_site_streamlit.py         # Main Streamlit app
├── urls.csv                           # Phishing dataset
├── phishing.pkl                       # Trained ML model
├── requirements.txt                   # Python dependencies
└── README.md                          # Project documentation
```

---

## How to Run the App

### 1. Clone the Repo
```bash
git clone https://github.com/kathyareddy/Adaptive-Firewall-System.git
cd Adaptive-Firewall-System
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run phishing_site_streamlit.py
```

### 4. UFW Setup (Linux Only)

Make sure UFW is enabled and your user has sudo privileges:

```bash
sudo ufw enable
```

>  Note: The app uses `os.system()` calls to execute UFW commands. These may require root access. Ensure you run the app on a secure environment.

---

## Model Info

- **Algorithm**: Random Forest Classifier  
- **Dataset**: 11 features extracted from URLs (`urls.csv`)  
- **Accuracy**: ~96% on test data  
- **Output**: Binary classification – `phishing` or `legitimate`  

---

## Sample Features from Dataset

- Having_IP_Address  
- URL_Length  
- Having_At_Symbol  
- Prefix_Suffix  
- DNS_Record  
- Web_Traffic  
- ... (Total 11)

---


## Future Improvements

- Real-time URL scanning via browser extension or proxy
- Deploy on cloud/VPS for scalable protection
- Log blocked IPs with timestamp
- Use advanced threat intel feeds

---

