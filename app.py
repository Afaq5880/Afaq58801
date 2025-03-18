import streamlit as st  # type: ignore
from model import predict_pr_approval

st.set_page_config(page_title="Singapore PR Approval Prediction", layout="wide")

st.title("Singapore PR Approval Prediction")
st.write("Enter your details below to get an estimated approval percentage.")

# Collect user inputs
age = st.slider("Age", 18, 60, 30)
nationality = st.selectbox("Nationality", ["Malaysia", "India", "Other"])
work_pass = st.selectbox("Work Pass Type", ["EP", "S Pass", "Work Permit"])
salary = st.number_input("Salary (SGD per month)", min_value=3000, step=100, value=5000)
education = st.selectbox("Education Level", ["PhD", "Masters", "Degree", "Diploma"])
institution = st.selectbox("Institution Attended", ["NUS", "NTU", "SMU", "Overseas"])
years_in_sg = st.slider("Years in SG", 0, 20, 5)
marital_status = st.selectbox("Marital Status", ["Married", "Single"])
children = st.number_input("Number of Children (SC/PR)", min_value=0, step=1, value=0)
employer = st.selectbox("Employer Reputation", ["MNC", "GLC", "SME", "Unknown"])
industry = st.selectbox("Industry Sector", ["Tech", "Finance", "Healthcare", "Others"])
community_involvement = st.selectbox("Community Involvement", ["Yes", "No"])
past_rejection = st.selectbox("Previous PR Application", ["None", "Rejected <1yr", "Rejected >1yr"])
language_proficiency = st.selectbox("Language Proficiency", ["Fluent", "Basic", "None"])

# Prediction button
if st.button("Predict PR Approval Chance"):
    user_profile = {
        "age": age,
        "nationality": nationality,
        "work_pass": work_pass,
        "salary": salary,
        "education": education,
        "institution": institution,
        "years_in_sg": years_in_sg,
        "marital": marital_status,
        "children": children,
        "employer": employer,
        "industry": industry,
        "community": community_involvement == "Yes",
        "rejected_before": past_rejection,
        "language": language_proficiency
    }

    score = predict_pr_approval(user_profile)
    st.subheader(f"Estimated PR Approval Chance: {score}%")
