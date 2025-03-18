import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def normalize_value(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0

def age_score(age):
    return 1 if 25 <= age <= 45 else 0.5

def predict_pr_approval(profile):
    weights = {
        "age": 0.05, "nationality": 0.05, "work_pass": 0.1, "salary": 0.1,
        "education": 0.1, "institution": 0.05, "years_in_sg": 0.1, "marital": 0.05,
        "children": 0.05, "employer": 0.05, "industry": 0.05, "community": 0.05,
        "rejected_before": 0.05, "language": 0.05
    }

    scoring_criteria = {
        "nationality": {"Malaysia": 1, "India": 0.7, "Other": 0.5},
        "work_pass": {"EP": 1, "S Pass": 0.7, "Work Permit": 0.4},
        "education": {"PhD": 1, "Masters": 0.9, "Degree": 0.8, "Diploma": 0.6},
        "institution": {"NUS": 1, "NTU": 1, "SMU": 1, "Overseas": 0.7},
        "marital": {"Married": 1, "Single": 0.5},
        "employer": {"MNC": 1, "GLC": 0.9, "SME": 0.7, "Other": 0.5},
        "industry": {"Tech": 1, "Finance": 1, "Healthcare": 1, "Other": 0.6},
        "community": {True: 1, False: 0},
        "rejected_before": {"None": 1, "Rejected >1yr": 0.7, "Rejected <1yr": 0.4},
        "language": {"Fluent": 1, "Basic": 0.6, "None": 0.3}
    }
    
    score = 0
    
    # Age component
    score += age_score(profile.get("age", 30)) * weights["age"]
    
    # Salary component
    salary = profile.get("salary", 5000)
    salary_score = 1 if salary >= 10000 else 0.8 if salary >= 6000 else 0.5
    score += salary_score * weights["salary"]
    
    # Years in SG component
    years_in_sg = profile.get("years_in_sg", 5)
    years_score = 1 if years_in_sg >= 5 else 0.8 if years_in_sg >= 2 else 0.4
    score += years_score * weights["years_in_sg"]
    
    # Categorical variables
    categorical_scores = {}
    for key, mapping in scoring_criteria.items():
        category_score = mapping.get(profile.get(key, "Other"), 0.5) * weights[key]
        categorical_scores[key] = category_score
        score += category_score
    
    # Log scores
    logging.info(f"Processed User Profile: {profile}")
    logging.info(f"Score Breakdown: Age({age_score(profile.get('age', 30))}), Salary({salary_score}), Years in SG({years_score}), Categorical({categorical_scores})")
    
    return round(score * 100, 2)
