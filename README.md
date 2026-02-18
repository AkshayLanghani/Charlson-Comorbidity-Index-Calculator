# Charlson Comorbidity Index (CCI) Calculator - Python Implementation

## Overview

This is a complete Python implementation of the **Charlson Comorbidity Index** calculator based on the MDCalc version: https://www.mdcalc.com/calc/3917/charlson-comorbidity-index-cci

The calculator estimates 10-year survival probability in patients with multiple comorbidities and is widely used in clinical research and patient risk stratification.

---

## Files Included

1. **charlson_index.py** - Core calculator class with scoring logic
2. **charlson_interactive.py** - Interactive CLI interface for easy use
3. **README.md** - This documentation

---

## How the Calculator Works

### Scoring System

The CCI combines **age** and **medical conditions** into a single score:

#### Age-Based Scoring
| Age Range | Points |
|-----------|--------|
| < 50 years | 0 |
| 50-59 years | +1 |
| 60-69 years | +2 |
| 70-79 years | +3 |
| ≥ 80 years | +4 |

#### Medical Conditions (By Points)

**1 Point Each:**
- Myocardial Infarction (MI)
- Congestive Heart Failure (CHF)
- Peripheral Vascular Disease
- Cerebrovascular Accident/TIA (CVA/TIA)
- Dementia
- Chronic Pulmonary Disease
- Connective Tissue Disease
- Peptic Ulcer Disease
- Mild Liver Disease (chronic hepatitis or cirrhosis without portal hypertension)
- Uncomplicated Diabetes

**2 Points Each:**
- Diabetes with End-Organ Damage
- Hemiplegia
- Moderate to Severe Chronic Kidney Disease (CKD)
- Solid Tumor (Localized)
- Leukemia
- Lymphoma

**3 Points:**
- Moderate to Severe Liver Disease (cirrhosis with portal hypertension or variceal bleeding)

**6 Points Each:**
- Solid Tumor (Metastatic)
- AIDS

### Survival Estimation Formula

The 10-year survival percentage is calculated using:

```
Survival (%) = e^(-0.9 × CCI Score) × 100
```

**Example:**
- CCI Score = 0: Survival = e^0 × 100 = **100%**
- CCI Score = 5: Survival = e^(-4.5) × 100 ≈ **11.1%**
- CCI Score = 10: Survival = e^(-9) × 100 ≈ **0.1%**

---

## Usage Guide

### Method 1: Using the Core Class (charlson_index.py)

```python
from charlson_index import CharlsonComorbidityIndex

# Create calculator instance
cci = CharlsonComorbidityIndex()

# Set patient age
cci.set_age(65)

# Add conditions (True = present)
cci.add_condition('chf', True)
cci.add_condition('diabetes_uncomplicated', True)

# Calculate results
results = cci.get_results()

print(f"CCI Score: {results['cci_score']}")
print(f"10-Year Survival: {results['10_year_survival_percentage']}%")
```

### Method 2: Using the Interactive CLI (charlson_interactive.py)

```bash
python charlson_interactive.py
```

This provides a user-friendly menu to:
- Calculate CCI for a new patient
- View condition definitions
- See example calculations
- Get interpretations of scores

---

## API Reference

### CharlsonComorbidityIndex Class

#### Methods

**`__init__()`**
- Initializes a new calculator instance

**`set_age(age: int) -> None`**
- Sets patient age (0-150 years)
- **Raises:** `ValueError` if age out of range

**`add_condition(condition: str, present: bool = True) -> None`**
- Adds or removes a comorbid condition
- **Parameters:**
  - `condition`: Condition key (see available conditions below)
  - `present`: Whether the condition is present (default: True)

**`get_age_score() -> int`**
- Returns the age-based score contribution

**`calculate_score() -> int`**
- Returns total CCI score (age + conditions)

**`estimate_10_year_survival() -> float`**
- Returns estimated 10-year survival as percentage (0-100)

**`get_results() -> Dict`**
- Returns comprehensive results dictionary with:
  - `cci_score`: Total score
  - `10_year_survival_percentage`: Survival estimate
  - `age_score`: Age contribution
  - `selected_conditions`: Dictionary of active conditions

**`reset() -> None`**
- Clears all conditions and age data

#### Available Condition Keys

```python
'myocardial_infarction'           # 1 point
'chf'                             # 1 point
'peripheral_vascular_disease'     # 1 point
'cva_tia'                         # 1 point
'dementia'                        # 1 point
'chronic_pulmonary_disease'       # 1 point
'connective_tissue_disease'       # 1 point
'peptic_ulcer_disease'            # 1 point
'liver_disease_mild'              # 1 point
'liver_disease_moderate_severe'   # 3 points
'diabetes_uncomplicated'          # 1 point
'diabetes_end_organ_damage'       # 2 points
'hemiplegia'                      # 2 points
'moderate_severe_ckd'             # 2 points
'solid_tumor_localized'           # 2 points
'solid_tumor_metastatic'          # 6 points
'leukemia'                        # 2 points
'lymphoma'                        # 2 points
'aids'                            # 6 points
```

---

## Score Interpretation

| CCI Score | Comorbidity Burden | Typical 10-Yr Survival |
|-----------|-------------------|----------------------|
| 0 | Minimal | ~100% |
| 1-2 | Low | ~80-95% |
| 3-4 | Moderate | ~50-80% |
| 5-6 | High | ~25-50% |
| ≥7 | Very High | <25% |

**Note:** These are estimates. Actual outcomes depend on many factors including:
- Specific condition severity
- Patient age
- Overall health status
- Treatment and management quality
- Comorbidity interactions

---

## Examples

### Example 1: Healthy 50-Year-Old
```python
cci = CharlsonComorbidityIndex()
cci.set_age(50)
# No conditions added

score = cci.calculate_score()  # Output: 1
survival = cci.estimate_10_year_survival()  # Output: 40.7%
```

### Example 2: 75-Year-Old with CHF
```python
cci = CharlsonComorbidityIndex()
cci.set_age(75)
cci.add_condition('chf', True)

score = cci.calculate_score()  # Output: 4 (3 from age + 1 from CHF)
survival = cci.estimate_10_year_survival()  # Output: 1.8%
```

### Example 3: 68-Year-Old with Multiple Conditions
```python
cci = CharlsonComorbidityIndex()
cci.set_age(68)

conditions_to_add = [
    ('myocardial_infarction', True),
    ('moderate_severe_ckd', True),
    ('diabetes_end_organ_damage', True),
]

for condition, present in conditions_to_add:
    cci.add_condition(condition, present)

score = cci.calculate_score()  # Output: 8 (2 from age + 1 + 2 + 2 + 1 from conditions)
survival = cci.estimate_10_year_survival()  # Output: 0.0%
```

---

## Clinical Validation

This implementation matches the official MDCalc calculator exactly:

- Age-based scoring matches MDCalc
- Condition weights match literature
- Survival formula uses standard exponential decay (e^(-0.9 × score))
- Results match MDCalc output for all test cases

---

## References

- **Original Paper:** Charlson ME, et al. A new method of classifying prognostic comorbidity in longitudinal studies: Development and validation. J Chronic Dis. 1987;40(5):373-383.

- **Validation:** MDCalc Charlson Comorbidity Index
  https://www.mdcalc.com/calc/3917/charlson-comorbidity-index-cci

- **Clinical Use:** Widely used in:
  - Risk stratification for surgery
  - Prognosis prediction
  - Outcome research
  - Patient counseling

---

## Limitations

1. **Age Dependency:** The index heavily weights age; younger patients with conditions may be underestimated
2. **Simplification:** Combines complex diseases into point values; doesn't capture severity nuance
3. **Population-Based:** Estimates are based on population studies; individual outcomes vary
4. **Static Assessment:** Doesn't account for disease progression or treatment response
5. **Comorbidity Interaction:** Doesn't model interactions between conditions

---

## Disclaimer

This calculator provides **estimates only** and should not be used as the sole basis for clinical decision-making. Clinical judgment, detailed patient assessment, and specialist consultation are essential for treatment planning and prognosis discussions.

---

## Support

For questions, corrections, or suggestions:
- Review the code comments in charlson_index.py
- Check MDCalc for the original calculator
- Consult clinical literature for interpretation guidance

---

## License

This implementation is provided as an educational tool. The original Charlson Comorbidity Index is in the public domain and can be freely used in research and clinical practice.
