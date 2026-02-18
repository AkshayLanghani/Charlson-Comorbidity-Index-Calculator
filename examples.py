from charlson_index import CharlsonComorbidityIndex


def example_1_healthy_patient():
    print("\n" + "="*70)
    print("EXAMPLE 1: Healthy 45-Year-Old Patient".center(70))
    print("="*70)
    
    cci = CharlsonComorbidityIndex()
    cci.set_age(45)
    
    print("\nPatient Profile:")
    print("  Age: 45 years")
    print("  Comorbidities: None")
    
    results = cci.get_results()
    print(f"\nResults:")
    print(f"  CCI Score: {results['cci_score']}")
    print(f"  10-Year Survival: {results['10_year_survival_percentage']}%")
    print(f"  Interpretation: Excellent prognosis with minimal comorbidity burden")


def example_2_type_2_diabetes_patient():
    print("\n" + "="*70)
    print("EXAMPLE 2: Type 2 Diabetes Patient".center(70))
    print("="*70)
    
    cci = CharlsonComorbidityIndex()
    cci.set_age(62)
    cci.add_condition('diabetes_uncomplicated', True)
    
    print("\nPatient Profile:")
    print("  Age: 62 years")
    print("  Comorbidities: Type 2 Diabetes (diet-controlled)")
    
    results = cci.get_results()
    print(f"\nResults:")
    print(f"  CCI Score: {results['cci_score']}")
    print(f"  10-Year Survival: {results['10_year_survival_percentage']}%")
    print(f"  Interpretation: Low comorbidity burden with good prognosis")


def example_3_post_mi_with_chf():
    print("\n" + "="*70)
    print("EXAMPLE 3: Post-MI Patient with Heart Failure".center(70))
    print("="*70)
    
    cci = CharlsonComorbidityIndex()
    cci.set_age(68)
    cci.add_condition('myocardial_infarction', True)
    cci.add_condition('chf', True)
    cci.add_condition('chronic_pulmonary_disease', True)
    
    print("\nPatient Profile:")
    print("  Age: 68 years")
    print("  Comorbidities:")
    print("    - History of Myocardial Infarction")
    print("    - Congestive Heart Failure (NYHA III)")
    print("    - Chronic Obstructive Pulmonary Disease")
    
    results = cci.get_results()
    print(f"\nResults:")
    print(f"  CCI Score: {results['cci_score']}")
    print(f"  10-Year Survival: {results['10_year_survival_percentage']}%")
    print(f"  10-Year Mortality Risk: {100 - results['10_year_survival_percentage']:.1f}%")
    print(f"  Interpretation: High comorbidity burden - careful monitoring needed")
    print(f"  Recommendation: Consider cardiology referral, aggressive risk factor management")


def example_4_complex_geriatric_patient():
    print("\n" + "="*70)
    print("EXAMPLE 4: Complex Geriatric Patient".center(70))
    print("="*70)
    
    cci = CharlsonComorbidityIndex()
    cci.set_age(78)
    
    conditions_dict = {
        'myocardial_infarction': 'History of MI (2015)',
        'chf': 'Systolic Heart Failure (EF 35%)',
        'moderate_severe_ckd': 'CKD Stage 4 (eGFR 18)',
        'diabetes_end_organ_damage': 'Diabetes with diabetic nephropathy',
        'dementia': 'Mild cognitive impairment',
        'chronic_pulmonary_disease': 'COPD Gold Stage II',
    }
    
    for condition in conditions_dict.keys():
        cci.add_condition(condition, True)
    
    print("\nPatient Profile:")
    print("  Age: 78 years")
    print("  Comorbidities:")
    for condition, description in conditions_dict.items():
        print(f"    - {description}")
    
    results = cci.get_results()
    print(f"\nResults:")
    print(f"  CCI Score: {results['cci_score']}")
    print(f"  10-Year Survival: {results['10_year_survival_percentage']}%")
    print(f"  10-Year Mortality Risk: {100 - results['10_year_survival_percentage']:.1f}%")
    print(f"  \nInterpretation:")
    print(f"    Very high comorbidity burden. Limited life expectancy.")
    print(f"    Goals of care discussion recommended.")
    print(f"  Recommendations:")
    print(f"    - Palliative care consultation")
    print(f"    - Shared decision-making about interventions")
    print(f"    - Focus on quality of life and symptom management")


def example_5_cancer_patient():
    """Example 5: 72-year-old with metastatic cancer."""
    print("\n" + "="*70)
    print("EXAMPLE 5: Metastatic Cancer Patient".center(70))
    print("="*70)
    
    cci = CharlsonComorbidityIndex()
    cci.set_age(72)
    
    conditions = {
        'solid_tumor_metastatic': 'Stage IV Adenocarcinoma (lung, bone mets)',
        'moderate_severe_ckd': 'CKD Stage 3',
        'peptic_ulcer_disease': 'History of GI bleeding',
    }
    
    for condition in conditions.keys():
        cci.add_condition(condition, True)
    
    print("\nPatient Profile:")
    print("  Age: 72 years")
    print("  Comorbidities:")
    for condition, description in conditions.items():
        print(f"    - {description}")
    
    results = cci.get_results()
    print(f"\nResults:")
    print(f"  CCI Score: {results['cci_score']}")
    print(f"  10-Year Survival: {results['10_year_survival_percentage']}%")
    print(f"  \nInterpretation:")
    print(f"    Extremely limited survival. Metastatic malignancy dominates prognosis.")
    print(f"  Recommendations:")
    print(f"    - Oncology consultation if not already involved")
    print(f"    - Discuss realistic treatment goals")
    print(f"    - Consider clinical trial eligibility")
    print(f"    - Early palliative care involvement")


def example_6_comparing_patients():
    """Example 6: Compare two similar-aged patients with different comorbidities."""
    print("\n" + "="*70)
    print("EXAMPLE 6: Comparing Two Similar-Aged Patients".center(70))
    print("="*70)
    
    # Patient A: Minimal disease
    print("\n--- PATIENT A: Well-controlled chronic diseases ---")
    cci_a = CharlsonComorbidityIndex()
    cci_a.set_age(65)
    cci_a.add_condition('diabetes_uncomplicated', True)
    
    results_a = cci_a.get_results()
    print(f"  Age: 65, Condition: Uncomplicated Diabetes")
    print(f"  CCI Score: {results_a['cci_score']}")
    print(f"  10-Year Survival: {results_a['10_year_survival_percentage']}%")
    
    # Patient B: Multiple complications
    print("\n--- PATIENT B: Multiple serious conditions ---")
    cci_b = CharlsonComorbidityIndex()
    cci_b.set_age(65)
    cci_b.add_condition('diabetes_end_organ_damage', True)
    cci_b.add_condition('moderate_severe_ckd', True)
    cci_b.add_condition('myocardial_infarction', True)
    
    results_b = cci_b.get_results()
    print(f"  Age: 65, Conditions: Diabetes with nephropathy, CKD, MI history")
    print(f"  CCI Score: {results_b['cci_score']}")
    print(f"  10-Year Survival: {results_b['10_year_survival_percentage']}%")
    
    # Comparison
    print("\n--- COMPARISON ---")
    survival_diff = results_a['10_year_survival_percentage'] - results_b['10_year_survival_percentage']
    score_diff = results_b['cci_score'] - results_a['cci_score']
    print(f"  Score difference: +{score_diff} points (Patient B)")
    print(f"  Survival difference: {survival_diff:.1f}% worse for Patient B")
    print(f"  Clinical significance: Disease control and comorbidity management critical")


def example_7_prognostic_categories():
    """Example 7: Show how CCI stratifies risk."""
    print("\n" + "="*70)
    print("EXAMPLE 7: Risk Stratification by CCI Score".center(70))
    print("="*70)
    
    risk_categories = [
        (25, []),
        (55, ['chf']),
        (65, ['myocardial_infarction', 'chf', 'diabetes_uncomplicated']),
        (75, ['myocardial_infarction', 'chf', 'moderate_severe_ckd', 'diabetes_end_organ_damage']),
        (85, ['myocardial_infarction', 'chf', 'moderate_severe_ckd', 'aids']),
    ]
    
    print("\n" + "-"*70)
    print(f"{'Age':<6} {'Conditions':<40} {'Score':<8} {'Survival':<10}")
    print("-"*70)
    
    for age, conditions in risk_categories:
        cci = CharlsonComorbidityIndex()
        cci.set_age(age)
        for condition in conditions:
            cci.add_condition(condition, True)
        
        results = cci.get_results()
        condition_str = ', '.join([c.replace('_', ' ').title()[:20] for c in conditions]) or "None"
        
        print(f"{age:<6} {condition_str:<40} {results['cci_score']:<8} {results['10_year_survival_percentage']:>6.1f}%")
    
    print("-"*70)


def main():
    """Run all examples."""
    print("\n" + "█"*70)
    print("CHARLSON COMORBIDITY INDEX CALCULATOR - PRACTICAL EXAMPLES".center(70))
    print("█"*70)
    
    example_1_healthy_patient()
    example_2_type_2_diabetes_patient()
    example_3_post_mi_with_chf()
    example_4_complex_geriatric_patient()
    example_5_cancer_patient()
    example_6_comparing_patients()
    example_7_prognostic_categories()
    
    print("\n" + "█"*70)
    print("END OF EXAMPLES".center(70))
    print("█"*70 + "\n")


if __name__ == "__main__":
    main()
