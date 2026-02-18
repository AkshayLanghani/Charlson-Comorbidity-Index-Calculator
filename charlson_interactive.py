from charlson_index import CharlsonComorbidityIndex


def display_menu():
    print("\n" + "=" * 70)
    print("CHARLSON COMORBIDITY INDEX (CCI) CALCULATOR".center(70))
    print("=" * 70)
    print("\nOptions:")
    print("1. Calculate new patient CCI")
    print("2. View condition list and definitions")
    print("3. View examples")
    print("4. Quit")
    print("-" * 70)


def get_age_input() -> int:
    while True:
        try:
            age = int(input("\nEnter patient age (0-150): "))
            if 0 <= age <= 150:
                return age
            else:
                print("Please enter an age between 0 and 150.")
        except ValueError:
            print("Please enter a valid number.")


def select_conditions(cci: CharlsonComorbidityIndex) -> None:
    """Interactive condition selection."""
    
    conditions_menu = {
        '1': ('myocardial_infarction', 'Myocardial Infarction (MI) - 1 point'),
        '2': ('chf', 'Congestive Heart Failure (CHF) - 1 point'),
        '3': ('peripheral_vascular_disease', 'Peripheral Vascular Disease - 1 point'),
        '4': ('cva_tia', 'Cerebrovascular Accident/TIA - 1 point'),
        '5': ('dementia', 'Dementia - 1 point'),
        '6': ('chronic_pulmonary_disease', 'Chronic Pulmonary Disease - 1 point'),
        '7': ('connective_tissue_disease', 'Connective Tissue Disease - 1 point'),
        '8': ('peptic_ulcer_disease', 'Peptic Ulcer Disease - 1 point'),
        '9': ('liver_disease_mild', 'Liver Disease (Mild) - 1 point'),
        '10': ('liver_disease_moderate_severe', 'Liver Disease (Moderate/Severe) - 3 points'),
        '11': ('diabetes_uncomplicated', 'Diabetes (Uncomplicated) - 1 point'),
        '12': ('diabetes_end_organ_damage', 'Diabetes (End-Organ Damage) - 2 points'),
        '13': ('hemiplegia', 'Hemiplegia - 2 points'),
        '14': ('moderate_severe_ckd', 'Moderate/Severe CKD - 2 points'),
        '15': ('solid_tumor_localized', 'Solid Tumor (Localized) - 2 points'),
        '16': ('solid_tumor_metastatic', 'Solid Tumor (Metastatic) - 6 points'),
        '17': ('leukemia', 'Leukemia - 2 points'),
        '18': ('lymphoma', 'Lymphoma - 2 points'),
        '19': ('aids', 'AIDS - 6 points'),
    }
    
    print("\n" + "-" * 70)
    print("SELECT COMORBID CONDITIONS (enter condition numbers, separated by commas)")
    print("-" * 70)
    
    for key, (_, description) in conditions_menu.items():
        print(f"{key:>2}. {description}")
    
    print("\nEnter condition numbers (e.g., '1,2,5' for MI, CHF, and Dementia):")
    print("Leave blank for no conditions.")
    print("-" * 70)
    
    selection = input("Selection: ").strip()
    
    if selection:
        try:
            selected = [s.strip() for s in selection.split(',')]
            for choice in selected:
                if choice in conditions_menu:
                    condition_key, _ = conditions_menu[choice]
                    cci.add_condition(condition_key, True)
                else:
                    print(f"Warning: Invalid selection '{choice}' ignored.")
        except Exception as e:
            print(f"Error processing selection: {e}")


def calculate_patient_cci():
    cci = CharlsonComorbidityIndex()
    
    print("\n" + "=" * 70)
    print("NEW PATIENT ASSESSMENT".center(70))
    print("=" * 70)
    age = get_age_input()
    cci.set_age(age)
    select_conditions(cci)
    
    print("\n" + "=" * 70)
    print("RESULTS".center(70))
    print("=" * 70)
    
    results = cci.get_results()
    
    print(f"\nPatient Age: {age} years")
    print(f"Age Score: {results['age_score']} points")
    
    if results['selected_conditions']:
        print(f"\nSelected Conditions:")
        for condition, present in results['selected_conditions'].items():
            if present:
                score = cci.CONDITION_SCORES[condition]
                condition_display = condition.replace('_', ' ').title()
                print(f"  • {condition_display}: {score} point(s)")
    else:
        print(f"\nNo comorbid conditions selected")
    
    print("\n" + "-" * 70)
    print(f"TOTAL CCI SCORE: {results['cci_score']} points")
    print(f"ESTIMATED 10-YEAR SURVIVAL: {results['10_year_survival_percentage']}%")
    print("-" * 70)
    
    # Interpretation
    print("\nInterpretation:")
    score = results['cci_score']
    survival = results['10_year_survival_percentage']
    
    if score == 0:
        print("  • Score 0: Minimal comorbidity burden")
    elif score <= 2:
        print("  • Score 1-2: Low comorbidity burden")
    elif score <= 4:
        print("  • Score 3-4: Moderate comorbidity burden")
    elif score <= 6:
        print("  • Score 5-6: High comorbidity burden")
    else:
        print("  • Score ≥7: Very high comorbidity burden")
    
    print(f"  • Predicted 10-year all-cause mortality: {100 - survival:.1f}%")
    print("  • Higher scores indicate worse prognosis and higher mortality risk")


def view_condition_definitions():
    definitions = {
        'Myocardial Infarction': 'History of definite or probable MI (EKG changes and/or enzyme changes)',
        'CHF': 'Exertional or paroxysmal nocturnal dyspnea and responded to digitalis, diuretics, or afterload reducing agents',
        'Peripheral Vascular Disease': 'Intermittent claudication or past bypass for chronic arterial insufficiency, history of gangrene, or untreated thoracic/abdominal aneurysm (≥6 cm)',
        'CVA/TIA': 'History of cerebrovascular accident with minor/no residua and transient ischemic attacks',
        'Dementia': 'Chronic cognitive deficit',
        'Chronic Pulmonary Disease': 'Any chronic lung disease',
        'Connective Tissue Disease': 'Documented connective tissue disease',
        'Peptic Ulcer Disease': 'Any history of treatment for ulcer or history of bleeding',
        'Liver Disease (Mild)': 'Chronic hepatitis or cirrhosis without portal hypertension',
        'Liver Disease (Moderate/Severe)': 'Cirrhosis with portal hypertension or variceal bleeding',
        'Diabetes': 'Uncomplicated = diet/medication controlled; End-organ damage = complication with eye, kidney, or neurological involvement',
        'Hemiplegia': 'Paralysis of one side of the body',
        'Moderate to Severe CKD': 'Creatinine >3 mg/dL or on dialysis/transplant',
        'Solid Tumor': 'Localized = no distant metastases; Metastatic = distant spread present',
        'Leukemia': 'Any form of leukemia',
        'Lymphoma': 'Any form of lymphoma',
        'AIDS': 'Acquired immunodeficiency syndrome'
    }
    
    print("\n" + "=" * 70)
    print("CONDITION DEFINITIONS".center(70))
    print("=" * 70)
    
    for condition, definition in definitions.items():
        print(f"\n{condition}:")
        print(f"  {definition}")


def view_examples():
    print("\n" + "=" * 70)
    print("EXAMPLE CALCULATIONS".center(70))
    print("=" * 70)
    
    examples = [
        {
            'title': 'Healthy 40-Year-Old',
            'age': 40,
            'conditions': [],
        },
        {
            'title': '65-Year-Old with CHF and Diabetes',
            'age': 65,
            'conditions': [('chf', 'CHF'), ('diabetes_uncomplicated', 'Uncomplicated Diabetes')],
        },
        {
            'title': '75-Year-Old with Multiple Conditions',
            'age': 75,
            'conditions': [
                ('myocardial_infarction', 'MI'),
                ('chf', 'CHF'),
                ('chronic_pulmonary_disease', 'Chronic Pulmonary Disease'),
                ('moderate_severe_ckd', 'CKD'),
                ('diabetes_end_organ_damage', 'Diabetes with End-Organ Damage'),
            ],
        },
        {
            'title': '85-Year-Old with Metastatic Cancer',
            'age': 85,
            'conditions': [('solid_tumor_metastatic', 'Metastatic Cancer')],
        },
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n{i}. {example['title']}")
        print("-" * 70)
        
        cci = CharlsonComorbidityIndex()
        cci.set_age(example['age'])
        
        for condition_key, condition_name in example['conditions']:
            cci.add_condition(condition_key, True)
        
        results = cci.get_results()
        
        print(f"   Age: {example['age']}")
        if example['conditions']:
            print(f"   Conditions: {', '.join([name for _, name in example['conditions']])}")
        else:
            print(f"   Conditions: None")
        print(f"   CCI Score: {results['cci_score']}")
        print(f"   10-Year Survival: {results['10_year_survival_percentage']}%")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            calculate_patient_cci()
        elif choice == '2':
            view_condition_definitions()
        elif choice == '3':
            view_examples()
        elif choice == '4':
            print("\nThank you for using the Charlson Index Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
