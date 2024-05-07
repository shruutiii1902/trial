import streamlit as st

# Function to set background color
def set_background(color):
    hex_color = f'#{color}'
    css = f"""
        <style>
        .stApp {{
            background-color: {hex_color};
            color: white;
        }}
        </style>
    """
    st.markdown(css, unsafe_allow_html=True)


set_background("BA7ABC")

st.title("Are you looking for a job? then fill the below details")

# Input fields for personal details
st.markdown("Details")
full_name = st.text_input("Full Name")
email = st.text_input("Email ID")
mobile_number = st.text_input("Mobile Number")
resume = st.file_uploader("Upload Resume", type=["pdf", "docx"])

# Dropdown for education
education_options = ["10th", "12th", "Graduate", "Masters"]
education_level = st.selectbox("Education Level", education_options)

# Dropdown for completion status
completion_status_options = ["Pursuing", "Completed"]
completion_status = st.selectbox("Completion Status", completion_status_options)

 # Input fields for marks and grades
marks = None
grade = None
graduation_grade = None
if completion_status == "Completed":
    if education_level in ["10th", "12th"]:
        marks = st.number_input(f"{education_level} Marks", min_value=0, max_value=100)
    else:
        grade = st.text_input(f"{education_level} Grade")
    if education_level == "Masters":
        graduation_grade = st.text_input("Graduation Grade")
    if education_level == "Graduate" or education_level == "Masters":
        graduation_certificate = st.file_uploader("Upload Graduation Certificate", type=["pdf", "docx"])
    if education_level == "Masters":
            masters_certificate = st.file_uploader("Upload Masters Certificate", type=["pdf", "docx"])

# Input field for specialization
specialization = None
if education_level in ["Graduate", "Masters"]:
    specialization = st.text_input("Specialization")

# Dropdown for experience
experience_options = ["Yes", "No"]
experience = st.selectbox("Experience", experience_options)
years_experience = None
company_name = None
position = None
if experience == "Yes":
    years_experience = st.number_input("Years of Experience")
    company_name = st.text_input("Previous Company Name")
    position = st.text_input("Position")

skills = st.text_area("Skills")

# Button to trigger backend processing
if st.button("Submit", disabled=(not all([full_name, email, mobile_number, resume, education_level, completion_status]))):
    st.success("Thank you for submitting your details!")

