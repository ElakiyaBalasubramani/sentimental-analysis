import streamlit as st
import joblib
import base64

def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

#image file
image_path = r"c:\Users\91989\Music\DALL·E-1.webp"  

# Convert the image to Base64
encoded_image = get_base64_of_image(image_path)

# Set Background Image using CSS
page_bg_img = f"""
<style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load ML Model
model = joblib.load("logistic_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# UI Components
st.title("🎸 Online Product Reviews using Sentimental Analysis")
review = st.text_area("Enter your review:")

# Prediction
if st.button("Predict Sentiment"):
    if review.strip() != "":
        review_vector = vectorizer.transform([review])
        prediction = model.predict(review_vector)
        sentiment = "Positive 😊" if prediction[0] == 1 else "Negative 😞"
        st.success(f"Predicted Sentiment: {sentiment}")
    else:
        st.warning("⚠ Please enter a review to analyze.")