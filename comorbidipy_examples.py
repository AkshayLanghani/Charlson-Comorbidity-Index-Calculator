
import polars as pl
from comorbidipy import comorbidity, hfrs, disability


def example_1_basic_charlson():
    print("\n" + "="*70)
    print("EXAMPLE 1: Basic Charlson Score from ICD Codes")
    print("="*70)
    
    df = pl.DataFrame({
        "patient_id": ["P001", "P001", "P001", "P002", "P002"],
        "icd_code": [
            "I21",    # Myocardial infarction
            "I50",    # Heart failure
            "J44",    # COPD
            "E11",    # Type 2 diabetes
            "I10",    # Hypertension
        ],
        "age": [65, 65, 65, 72, 72],
    })
    
    print("\nInput Data (ICD Codes):")
    print(df)
    

    result = comorbidity(
        df,
        id_col="patient_id",
        code_col="icd_code",
        age_col="age"
    )
    
    print("\nCharlson Comorbidity Index Results:")
    print(result)
    
    print("\nInterpretation:")
    print("  - P001 (65yo): MI + Heart Failure + COPD = Higher mortality risk")
    print("  - P002 (72yo): Diabetes + Hypertension = Moderate risk")


def example_2_different_variants():
    print("\n" + "="*70)
    print("EXAMPLE 2: Charlson Variants (Quan, Swedish, Australian, SHMI)")
    print("="*70)
    
    df = pl.DataFrame({
        "patient_id": ["P001", "P002", "P003"],
        "icd_code": ["I21", "E11", "N18"],  # MI, Diabetes, CKD
        "age": [65, 70, 75],
    })
    
    variants = ["quan", "swedish", "australian", "shmi"]
    
    print("\nComparing different Charlson variants...")
    print("-"*70)
    
    for variant in variants:
        try:
            result = comorbidity(
                df,
                id_col="patient_id",
                code_col="icd_code",
                age_col="age",
                variant=variant
            )
            print(f"\n{variant.upper()} variant:")
            print(result.select(["patient_id", "charlson"]))
        except Exception as e:
            print(f"\n{variant.upper()}: {str(e)[:60]}")


def example_3_elixhauser():
    print("\n" + "="*70)
    print("EXAMPLE 3: Elixhauser Comorbidity Index")
    print("="*70)
    
    df = pl.DataFrame({
        "patient_id": ["P001", "P001", "P002", "P002", "P002"],
        "icd_code": [
            "I50",    # CHF
            "E11",    # Diabetes
            "F32",    # Depression
            "I10",    # Hypertension
            "K74",    # Cirrhosis
        ],
        "age": [60, 60, 70, 70, 70],
    })
    
    print("\nPatient Data:")
    print(df)
    
    try:
        from comorbidipy import elixhauser
        
        result = elixhauser(
            df,
            id_col="patient_id",
            code_col="icd_code",
            age_col="age"
        )
        
        print("\nElixhauser Results:")
        print(result)
    except ImportError:
        print("Note: Elixhauser may require additional setup")


def example_4_hospital_frailty_risk():
    """Example 4: Hospital Frailty Risk Score (HFRS) for elderly."""
    print("\n" + "="*70)
    print("EXAMPLE 4: Hospital Frailty Risk Score (≥75 years)")
    print("="*70)
    
    # Elderly patients data
    df = pl.DataFrame({
        "patient_id": ["P001", "P001", "P002", "P002"],
        "icd_code": [
            "R26",    # Abnormality of gait
            "R29",    # Abnormality of movement
            "I50",    # Heart failure
            "N18",    # CKD
        ],
        "age": [78, 78, 82, 82],
    })
    
    print("\nElderly Patient Data:")
    print(df)
    
    try:
        result = hfrs(
            df,
            id_col="patient_id",
            code_col="icd_code"
        )
        
        print("\nHospital Frailty Risk Score:")
        print(result)
        print("\nInterpretation:")
        print("  - HFRS identifies frailty indicators in elderly patients")
        print("  - Helps predict hospital outcomes for ≥75 year olds")
    except Exception as e:
        print(f"HFRS Example: {e}")


def example_5_disability_screening():
    """Example 5: Disability and Sensory Impairment Screening."""
    print("\n" + "="*70)
    print("EXAMPLE 5: Disability & Sensory Impairment Detection")
    print("="*70)
    
    df = pl.DataFrame({
        "patient_id": ["P001", "P001", "P002", "P002"],
        "icd_code": [
            "H54",    # Vision loss/blindness
            "H93",    # Hearing loss
            "F79",    # Intellectual disability
            "G82",    # Paralysis
        ],
    })
    
    print("\nPatient Data with Disability Codes:")
    print(df)
    
    try:
        result = disability(
            df,
            id_col="patient_id",
            code_col="icd_code"
        )
        
        print("\nDisability Screening Results:")
        print(result)
    except Exception as e:
        print(f"Disability screening: {e}")


def example_6_working_with_csv():
    """Example 6: Working with CSV files."""
    print("\n" + "="*70)
    print("EXAMPLE 6: Reading from CSV and Writing Results")
    print("="*70)
    
    # Create sample CSV data
    sample_csv_path = "sample_patient_data.csv"
    
    df_sample = pl.DataFrame({
        "patient_id": ["P001", "P001", "P002", "P002", "P003"],
        "icd_code": ["I21", "I50", "E11", "J44", "C34"],
        "age": [65, 65, 72, 72, 58],
        "admission_date": ["2025-01-01", "2025-01-01", "2025-01-15", "2025-01-15", "2025-02-01"],
    })
    
    # Save to CSV
    df_sample.write_csv(sample_csv_path)
    print(f"\nCreated sample file: {sample_csv_path}")
    
    # Read from CSV
    df = pl.read_csv(sample_csv_path)
    print("\nData loaded from CSV:")
    print(df)
    
    # Calculate scores
    result = comorbidity(
        df,
        id_col="patient_id",
        code_col="icd_code",
        age_col="age"
    )
    
    print("\nCharlson Scores:")
    print(result)
    
    # Save results
    output_path = "charlson_results.csv"
    result.write_csv(output_path)
    print(f"\nResults saved to: {output_path}")


def example_7_data_filtering():
    """Example 7: Advanced filtering and analysis."""
    print("\n" + "="*70)
    print("EXAMPLE 7: Data Filtering and Analysis")
    print("="*70)
    
    # Create larger dataset
    df = pl.DataFrame({
        "patient_id": ["P001", "P001", "P001", "P002", "P002", "P003", "P003"],
        "icd_code": ["I21", "I50", "J44", "E11", "I10", "F32", "K74"],
        "age": [65, 65, 65, 72, 72, 55, 55],
        "department": ["Cardiology", "Cardiology", "Respiratory", "Endocrine", "Cardiology", "Psychiatry", "Gastroenterology"],
    })
    
    print("\nFull Dataset:")
    print(df)
    
    # Calculate scores
    result = comorbidity(
        df,
        id_col="patient_id",
        code_col="icd_code",
        age_col="age"
    )
    
    print("\nCharlson Scores by Patient:")
    unique_patients = result.group_by("patient_id").agg([
        pl.col("charlson").first().alias("charlson_score")
    ])
    print(unique_patients)
    
    print("\nScore Statistics:")
    print(f"  - Mean score: {unique_patients['charlson_score'].mean():.1f}")
    print(f"  - Max score: {unique_patients['charlson_score'].max()}")
    print(f"  - Min score: {unique_patients['charlson_score'].min()}")


def main():
    """Run all examples."""
    print("\n" + "█"*70)
    print("COMORBIDIPY - PRACTICAL EXAMPLES".center(70))
    print("█"*70)
    
    try:
        example_1_basic_charlson()
    except Exception as e:
        print(f"Example 1 Note: {e}")
    
    try:
        example_2_different_variants()
    except Exception as e:
        print(f"Example 2 Note: {e}")
    
    try:
        example_3_elixhauser()
    except Exception as e:
        print(f"Example 3 Note: {e}")
    
    try:
        example_4_hospital_frailty_risk()
    except Exception as e:
        print(f"Example 4 Note: {e}")
    
    try:
        example_5_disability_screening()
    except Exception as e:
        print(f"Example 5 Note: {e}")
    
    try:
        example_6_working_with_csv()
    except Exception as e:
        print(f"Example 6 Note: {e}")
    
    try:
        example_7_data_filtering()
    except Exception as e:
        print(f"Example 7 Note: {e}")
    
    print("\n" + "█"*70)
    print("END OF EXAMPLES".center(70))
    print("█"*70 + "\n")


if __name__ == "__main__":
    main()
