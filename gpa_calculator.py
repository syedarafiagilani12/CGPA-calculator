import streamlit as st

st.title("🎓 GPA & CGPA Calculator")

# Mapping grades to points
grade_points = {
    "A": 4.0,
    "A-": 3.66,
    "B+": 3.33,
    "B": 3.0,
    "B-": 2.66,
    "C+": 2.33,
    "C": 2.0,
    "C-": 1.66,
    "D+": 1.33,
    "D": 1.0,
    "F": 0.0
}

st.header("📚 Current Semester")

num_courses = st.number_input("Number of courses this semester", min_value=1, max_value=20, step=1)

current_grades = []
current_credits = []

for i in range(int(num_courses)):
    col1, col2 = st.columns(2)
    with col1:
        grade = st.selectbox(f"Grade for Course {i+1}", list(grade_points.keys()), key=f"grade_{i}")
    with col2:
        credit = st.number_input(f"Credit Hours for Course {i+1}", min_value=0.0, step=0.5, key=f"credit_{i}")
    current_grades.append(grade_points[grade])
    current_credits.append(credit)

# GPA Calculation
def calculate_gpa(grades, credits):
    total_points = sum(g * c for g, c in zip(grades, credits))
    total_credits = sum(credits)
    if total_credits == 0:
        return 0.0
    return total_points / total_credits

current_gpa = calculate_gpa(current_grades, current_credits)
st.success(f"🎯 GPA for Current Semester: **{current_gpa:.2f}**")

# Previous semesters
st.header("🕒 Previous Semesters (for CGPA)")

num_prev = st.number_input("Number of previous semesters", min_value=0, max_value=20, step=1)

prev_gpas = []
prev_credits = []

for i in range(int(num_prev)):
    col1, col2 = st.columns(2)
    with col1:
        gpa = st.number_input(f"GPA of Semester {i+1}", min_value=0.0, max_value=4.0, step=0.01, key=f"prev_gpa_{i}")
    with col2:
        credit = st.number_input(f"Total Credits in Semester {i+1}", min_value=0.0, step=0.5, key=f"prev_credit_{i}")
    prev_gpas.append(gpa)
    prev_credits.append(credit)

# CGPA Calculation
total_prev_points = sum(g * c for g, c in zip(prev_gpas, prev_credits))
total_prev_credits = sum(prev_credits)

total_current_points = current_gpa * sum(current_credits)
total_current_credits = sum(current_credits)

cgpa = 0.0
if (total_prev_credits + total_current_credits) > 0:
    cgpa = (total_prev_points + total_current_points) / (total_prev_credits + total_current_credits)

st.success(f"🏆 CGPA: **{cgpa:.2f}**")

