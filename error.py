import streamlit as st
def set_background(color):
    hex_color = f'#{color}'
    css = f"""
        <style>
        .stApp {{
            background-color: {hex_color};
        }}
        </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set imperial background color
set_background("602f6b")  # Example color code, adjust as needed

# Function to initialize session state
def init_session_state():
    if 'page' not in st.session_state:
        st.session_state.page = 'personal_details'
        st.session_state.full_name = ''
        st.session_state.email_id = ''
        st.session_state.password = ''
        st.session_state.mobile_number = ''
        st.session_state.work_status = ''
        st.session_state.education= ''
        st.session_state.course= ''
        st.session_state.skills = ''

# Function to navigate to the next page
def next_page():
    if st.session_state.page == 'personal_details':
        st.session_state.page = 'education_details'
    elif st.session_state.page == 'education_details':
        st.session_state.page = 'skills'

# Function to navigate to the previous page
def previous_page():
    if st.session_state.page == 'education_details':
        st.session_state.page = 'personal_details'
    elif st.session_state.page == 'skills':
        st.session_state.page = 'education_details'

# Main function to display the current page
def main():
    init_session_state()

    if st.session_state.page == 'personal_details':
        st.title('Personal Details')
        st.session_state.full_name = st.text_input("Full Name")
        st.session_state.email_id = st.text_input('Email Id')
        st.session_state.password = st.text_input('Password')
        st.session_state.mobile_number = st.text_input('Mobile number*')
        st.session_state.work_status = st.selectbox("Work Status*",["Experienced","Fresher"])
        if st.button('Next'):
            next_page()

    elif st.session_state.page == 'education_details':
        st.title('Education Details')
        st.session_state.education = st.selectbox('Highest Qualification/Degree pursuing*', ['10th', '12th', 'Graduation/Diploma', 'Masters/Post-graduation', 'Doctorate/PhD'])
        st.session_state.course = st.selectbox('Course*', ['B.A', 'BCA', 'B.B.A/B.M.S', 'B.Com', 'B.Ed', 'B.Pharma', 'B.Sc', 'B.Tech', 'B.E.', 'LLB', 'Diploma', 'CA', 'CS', 'Integrated PG', 'M.A', 'M.Com', 'M.S/M.Sc', 'M.Tech/PGDM', 'MCA', 'PD Diploma', 'Ph.D/Doctorate', 'MPHIL', 'Other Doctorate'])
        if st.button('Previous'):
            previous_page()
        elif st.button('Next'):
            next_page()

    elif st.session_state.page == 'skills':
        st.title('Skills')
        st.session_state.skills = st.text_area('Skills*')
        if st.button('Previous'):
            previous_page()
        elif st.button('Submit'):
            # You can perform actions such as submitting data to a database here
            st.success('Your details have been submitted successfully!')

if __name__ == '__main__':
    main()
