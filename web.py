import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
# from fpdf import FPDF
# import io

# Simulated prediction function (Replace with actual model prediction)
def predict_diabetic_retinopathy(image):
    prediction = np.random.choice([0, 1])  # 0 for No DR, 1 for DR
    confidence_score = np.random.rand()  # Random confidence score for demo purposes
    return prediction, confidence_score

# # Function to create PDF advice
# def create_pdf():
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, txt="Advice for Patients After Diagnosis", ln=True, align="C")
#     advice = """
#     Medical Management:
#     1. Regular Eye Exams:
#        - Schedule regular follow-up appointments with an ophthalmologist to monitor the progression of diabetic retinopathy.
#     2. Blood Sugar Control:
    #    - Work closely with your healthcare provider to maintain optimal blood sugar levels. This can slow the progression of retinopathy.
    # 3. Blood Pressure and Cholesterol Management:
    #    - Keep blood pressure and cholesterol levels under control through medication, diet, and lifestyle changes.
    # 4. Medications:
    #    - Adhere strictly to any prescribed medications, including insulin, oral hypoglycemics, antihypertensives, and cholesterol-lowering drugs.

    # Lifestyle and Dietary Changes:
    # 1. Healthy Diet:
    #    - Follow a balanced diet rich in vegetables, fruits, lean proteins, and whole grains. Avoid sugary foods and drinks to help control blood sugar levels.
    # 2. Exercise:
    #    - Engage in regular physical activity, as recommended by your healthcare provider, to help manage blood sugar levels and overall health.
    # 3. Smoking Cessation:
    #    - If you smoke, seek help to quit. Smoking can worsen diabetic retinopathy and overall health.

    # Specific Eye Care:
    # 1. Prompt Treatment:
    #    - If your ophthalmologist recommends treatment such as laser therapy, injections, or surgery, ensure you understand the procedures and follow through with the treatment plan.
    # 2. Protect Your Eyes:
    #    - Wear sunglasses to protect your eyes from harmful UV rays.
    # 3. Report Vision Changes:
    #    - Immediately report any changes in vision, such as blurred vision, floaters, or dark areas in your vision, to your ophthalmologist.

    # General Health Management:
    # 1. Stay Informed:
    #    - Educate yourself about diabetic retinopathy and diabetes management. Understanding your condition can empower you to take better care of your health.
    # 2. Mental Health Support:
    #    - Managing a chronic condition can be stressful. Seek support from mental health professionals, support groups, or counseling if needed.

    # Follow-Up Care:
    # 1. Regular Check-Ups:
    #    - Ensure regular check-ups with your primary care physician, endocrinologist, and ophthalmologist to monitor and manage your diabetes and related complications effectively.
    # 2. Adherence to Recommendations:
    #    - Follow all recommendations from your healthcare providers regarding diet, lifestyle, and medication.
    # """
    # for line in advice.split("\n"):
    #     pdf.cell(200, 10, txt=line, ln=True)
    # return pdf

# User credentials
USER_CREDENTIALS = {
    "user1": "password1",
    "user2": "password2"
}

def authenticate(username, password):
    return USER_CREDENTIALS.get(username) == password

# Streamlit application
st.title("Diabetic Retinopathy Prediction")

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if st.session_state['authenticated']:
    st.sidebar.write("You are logged in")
    if st.sidebar.button("Logout"):
        st.session_state['authenticated'] = False
        st.experimental_rerun()

else:
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if authenticate(username, password):
            st.session_state['authenticated'] = True
            st.experimental_rerun()
        else:
            st.sidebar.error("Invalid username or password")

if st.session_state['authenticated']:
    st.write("""
    ## Upload patient images
    (Note: In practice, these would be actual clinical images)
    """)

    # Allow multiple file uploads
    uploaded_files = st.file_uploader("Choose images", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

    if uploaded_files:
        if st.button('Identify Diagnosis'):
            progress_bar = st.progress(0)
            total_files = len(uploaded_files)
            for i, uploaded_file in enumerate(uploaded_files):
                image = Image.open(uploaded_file)
                st.image(image, caption=f'Uploaded Image: {uploaded_file.name}', use_column_width=True)
                input_data = np.random.rand(1, 5)
                prediction, confidence_score = predict_diabetic_retinopathy(input_data)
                rounded_confidence_score = round(confidence_score, 4)
                confidence_scores = [round((1 - confidence_score), 4), rounded_confidence_score]
                binary_class = ["No DR", "DR"]
                st.write(f"### Confidence Scores for {uploaded_file.name}")
                st.bar_chart(pd.DataFrame({"Confidence Score": confidence_scores}, index=binary_class))
                if prediction == 1:
                    st.success(f"The model predicts Diabetic Retinopathy for {uploaded_file.name} with a confidence score of {rounded_confidence_score:.4f}.")
                else:
                    st.success(f"The model predicts No Diabetic Retinopathy for {uploaded_file.name} with a confidence score of {rounded_confidence_score:.4f}.")
                progress = (i + 1) / total_files
                progress_bar.progress(progress)
                time.sleep(0.1)
            st.success("Processing complete!")

            st.write("## Advice for Patients After Diagnosis")
            advice_text = """
            ### Medical Management:
            1. **Regular Eye Exams**:
               - Schedule regular follow-up appointments with an ophthalmologist to monitor the progression of diabetic retinopathy.
            2. **Blood Sugar Control**:
               - Work closely with your healthcare provider to maintain optimal blood sugar levels. This can slow the progression of retinopathy.
            3. **Blood Pressure and Cholesterol Management**:
               - Keep blood pressure and cholesterol levels under control through medication, diet, and lifestyle changes.
            4. **Medications**:
               - Adhere strictly to any prescribed medications, including insulin, oral hypoglycemics, antihypertensives, and cholesterol-lowering drugs.

            ### Lifestyle and Dietary Changes:
            1. **Healthy Diet**:
               - Follow a balanced diet rich in vegetables, fruits, lean proteins, and whole grains. Avoid sugary foods and drinks to help control blood sugar levels.
            2. **Exercise**:
               - Engage in regular physical activity, as recommended by your healthcare provider, to help manage blood sugar levels and overall health.
            3. **Smoking Cessation**:
               - If you smoke, seek help to quit. Smoking can worsen diabetic retinopathy and overall health.

            ### Specific Eye Care:
            1. **Prompt Treatment**:
               - If your ophthalmologist recommends treatment such as laser therapy, injections, or surgery, ensure you understand the procedures and follow through with the treatment plan.
            2. **Protect Your Eyes**:
               - Wear sunglasses to protect your eyes from harmful UV rays.
            3. **Report Vision Changes**:
               - Immediately report any changes in vision, such as blurred vision, floaters, or dark areas in your vision, to your ophthalmologist.

            ### General Health Management:
            1. **Stay Informed**:
               - Educate yourself about diabetic retinopathy and diabetes management. Understanding your condition can empower you to take better care of your health.
            2. **Mental Health Support**:
               - Managing a chronic condition can be stressful. Seek support from mental health professionals, support groups, or counseling if needed.

            ### Follow-Up Care:
            1. **Regular Check-Ups**:
               - Ensure regular check-ups with your primary care physician, endocrinologist, and ophthalmologist to monitor and manage your diabetes and related complications effectively.
            2. **Adherence to Recommendations**:
               - Follow all recommendations from your healthcare providers regarding diet, lifestyle, and medication.
            """
            st.write(advice_text)

            # pdf = create_pdf()
            # pdf_output = io.BytesIO()
            # pdf.output(pdf_output)
            # pdf_output.seek(0)

            st.download_button(
                label="Download Advice as PDF",
                data=pdf_output,
                file_name="Diabetic_Retinopathy_Advice.pdf",
                mime="application/pdf"
            )
else:
    st.write("Please log in to use the application.")
