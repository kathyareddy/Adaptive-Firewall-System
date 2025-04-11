# streamlit_app.py
import streamlit as st
import joblib
import pandas as pd
from urllib.parse import urlparse
import socket
import tldextract
import re
import numpy as np

# Function to extract features from the URL
def extract_features(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.netloc
    features = {}

    # URL length
    features['length_url'] = len(url)

    # Hostname length
    features['length_hostname'] = len(parsed_url.hostname) if parsed_url.hostname else 0

    # Extract IP address
    try:
        socket.gethostbyname(parsed_url.hostname)
        features['ip'] = 1
    except Exception:
        features['ip'] = 0

    # Number of dots, question marks, equal signs, and slashes
    features['nb_dots'] = url.count('.')
    features['nb_qm'] = url.count('?')
    features['nb_eq'] = url.count('=')
    features['nb_slash'] = url.count('/')
    features['nb_www'] = url.count('www')

    # Ratio of digits in URL and hostname
    features['ratio_digits_url'] = sum(c.isdigit() for c in url) / len(url) if len(url) > 0 else 0
    features['ratio_digits_host'] = sum(c.isdigit() for c in parsed_url.hostname) / len(parsed_url.hostname) if parsed_url.hostname else 0

    # TLD in subdomain and prefix-suffix
    extracted = tldextract.extract(url)
    features['tld_in_subdomain'] = 1 if extracted.subdomain and extracted.suffix in extracted.subdomain else 0
    features['prefix_suffix'] = 1 if re.match(r'^(www|mail|ftp)', extracted.subdomain) else 0

    # Longest word in URL and path
    path_words = parsed_url.path.split('/')
    features['longest_word_path'] = max((len(word) for word in path_words), default=0)
    features['longest_words_raw'] = max((len(word) for word in hostname.split('.')), default=0)

    # Phishing hints based on keyword matching
    phishing_keywords = ['secure', 'account', 'verify', 'update', 'confirm']
    features['phish_hints'] = 1 if any(keyword in url.lower() for keyword in phishing_keywords) else 0

    return features

# Streamlit app
def main():
    st.title("Phishing URL Detection")

    # Input URL from user
    url = st.text_input("Enter a URL for phishing detection")

    # Load the pre-trained model and scaler
    model = joblib.load('/home/ubuntu/ann/firewall_model.pkl')
    scaler = joblib.load('/home/ubuntu/ann/scaler.pkl')

 # Define the feature names expected by the scaler
    feature_names = [
        'length_url',
        'length_hostname',
        'ip',
        'nb_dots',
        'nb_qm',
        'nb_eq',
        'nb_slash',
        'nb_www',
        'ratio_digits_url',
        'ratio_digits_host',
        'tld_in_subdomain',
        'prefix_suffix',
        'longest_words_raw',
        'longest_word_path',
        'phish_hints',
    ]

    # Prediction button
    if st.button("Predict"):
        if url:
            # Extract features from the input URL
            features = extract_features(url)
            feature_list = [features[name] for name in feature_names]

            # Create DataFrame with correct columns
            feature_df = pd.DataFrame([feature_list], columns=feature_names)

            # Scale the feature set
            scaled_features = scaler.transform(feature_df)

            # Predict the URL's legitimacy
            prediction = model.predict(scaled_features)
            result = "Phishing" if prediction[0] == 1 else "Legitimate"

            # Display result
            st.success(f"The URL is predicted to be: {result}")
        else:
            st.error("Please enter a valid URL.")

if __name__ == "__main__":
    main()
