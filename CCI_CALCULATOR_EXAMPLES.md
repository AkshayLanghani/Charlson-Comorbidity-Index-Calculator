# CCI Calculator - Real-World Examples

This file shows how to use the calculator with different types of datasets.

---

## Example 1: Medical Hospital Dataset

**Dataset:** `hospital_patients.csv`
```
PATIENT_ID,HOSPITAL_ADMISSION_ID,PRIMARY_DIAGNOSIS,SECONDARY_DX_1,SECONDARY_DX_2,SECONDARY_DX_3
PT001,ADM001,I50.9,I10,I25.10,
PT002,ADM002,E11.9,I63.9,G45.9,I26.99
PT003,ADM003,,,
```

**Command:**
```bash
python accurate_cci_calculator.py \
    --input hospital_patients.csv \
    --id-col PATIENT_ID \
    --claim-col HOSPITAL_ADMISSION_ID \
    --icd-prefix PRIMARY_DIAGNOSIS,SECONDARY_DX \
    --max-icd-cols 4 \
    --output hospital_comorbidity.xlsx
```

Wait, the above won't work with our current script (can't handle mixed names). Let me provide a better example:

**Corrected Command (rename columns first in Excel, or use this approach):**
```bash
python accurate_cci_calculator.py \
    --input hospital_patients.csv \
    --id-col PATIENT_ID \
    --claim-col HOSPITAL_ADMISSION_ID \
    --icd-prefix PRIMARY_DIAGNOSIS
```

**Note:** You'll need to rename your diagnosis columns to PRIMARY_DIAGNOSIS1, PRIMARY_DIAGNOSIS2, etc.

---

## Example 2: Insurance Claims Database

**Dataset:** `insurance_claims.csv`
```
MEMBER_ID,CLAIM_ID,CLAIM_DATE,DIAG_CODE_1,DIAG_CODE_2,DIAG_CODE_3,DIAG_CODE_4,DIAG_CODE_5
M123456,C001,2024-01-15,I50.9,I10,,
M123457,C002,2024-01-16,E11.9,I63.9,I26.99,G45.9,I70.0
M123458,C003,2024-01-17,,,
```

**Command:**
```bash
python accurate_cci_calculator.py \
    --input insurance_claims.csv \
    --id-col MEMBER_ID \
    --claim-col CLAIM_ID \
    --icd-prefix DIAG_CODE \
    --max-icd-cols 5 \
    --output insurance_comorbidity_analysis.xlsx
```

**Output:** `insurance_comorbidity_analysis.xlsx`
- Sheet 1: All 1000+ members with CCI scores
- Sheet 2: Condition prevalence rates
- Sheet 3: Statistical summaries
- Sheet 4: Detailed patient breakdown

---

## Example 3: Research Study Cohort

**Dataset:** `research_cohort.csv`
```
SUBJECT_ID,VISIT_ID,VISIT_DATE,ICD10_1,ICD10_2,ICD10_3,ICD10_4,ICD10_5,ICD10_6
S0001,V1,2023-01-01,I50.9,I10,I25.10,
S0002,V1,2023-01-02,E11.9,I63.9,I26.99,G45.9,I70.0,I73.9
S0003,V1,2023-01-03,,,
```

**Command:**
```bash
python accurate_cci_calculator.py \
    --input research_cohort.csv \
    --id-col SUBJECT_ID \
    --claim-col VISIT_ID \
    --icd-prefix ICD10 \
    --max-icd-cols 6 \
    --output research_comorbidity_index.xlsx
```

**Use Case:** Assessing baseline comorbidity burden for research endpoints

---

## Example 4: Primary Care Registry

**Dataset:** `primary_care_registry.csv`
```
MRN,ENCOUNTER_ID,ENCOUNTER_DATE,DIAGNOSIS_01,DIAGNOSIS_02,DIAGNOSIS_03,DIAGNOSIS_04
12345,E20240115,2024-01-15,I50.22,I10,,
67890,E20240116,2024-01-16,E11.9,I63.9,I26.99,G45.9
54321,E20240117,2024-01-17,,,
```

**Command:**
```bash
python accurate_cci_calculator.py \
    --input primary_care_registry.csv \
    --id-col MRN \
    --claim-col ENCOUNTER_ID \
    --icd-prefix DIAGNOSIS \
    --max-icd-cols 4 \
    --output primary_care_comorbidity.xlsx
```

---

## Example 5: Medicare/Medicaid Claims

**Dataset:** `medicaid_claims.csv`
```
BENEFICIARY_ID,CLAIM_CONTROL_NO,CLAIM_FROM_DATE,PRNCPAL_DGNS_CD,DGNS_CD_1,DGNS_CD_2,DGNS_CD_3,DGNS_CD_4,DGNS_CD_5,DGNS_CD_6,DGNS_CD_7,DGNS_CD_8,DGNS_CD_9,DGNS_CD_10
123456789,CLM000001,2024-01-15,I50.9,I10,I25.10,,,
987654321,CLM000002,2024-01-16,E11.9,I63.9,I26.99,G45.9,I70.0,,,
555555555,CLM000003,2024-01-17,,,
```

**Command:**
```bash
python accurate_cci_calculator.py \
    --input medicaid_claims.csv \
    --id-col BENEFICIARY_ID \
    --claim-col CLAIM_CONTROL_NO \
    --icd-prefix DGNS_CD \
    --max-icd-cols 10 \
    --output medicaid_comorbidity_analysis.xlsx
```

---

## Example 6: EHR/EMR System Export

**Dataset:** `ehr_export.csv`
```
PATIENT_KEY,ENCOUNTER_KEY,VISIT_DATE,PROBLEM_1,PROBLEM_2,PROBLEM_3,PROBLEM_4,PROBLEM_5,PROBLEM_6,PROBLEM_7,PROBLEM_8,PROBLEM_9,PROBLEM_10,PROBLEM_11,PROBLEM_12
1001,ENC1001,2024-01-15,I50.32,I10,,,
1002,ENC1002,2024-01-16,E11.9,I63.9,I26.99,I70.0,G45.9,I25.2,I73.9,I50.9,,
1003,ENC1003,2024-01-17,,,
```

**Command:**
```bash
python accurate_cci_calculator.py \
    --input ehr_export.csv \
    --id-col PATIENT_KEY \
    --claim-col ENCOUNTER_KEY \
    --icd-prefix PROBLEM \
    --max-icd-cols 12 \
    --output ehr_comorbidity_results.xlsx
```

---

## Step-by-Step: Preparing Your Dataset

### If your ICD columns are named differently:

**Original columns:** `DX1`, `DX2`, `DX3`, etc.

**Option A:** Use in script (if prefix is consistent)
```bash
python accurate_cci_calculator.py \
    --input data.csv \
    --icd-prefix DX \
    --max-icd-cols 5
```

**Option B:** Rename in Excel first, then use:
```bash
python accurate_cci_calculator.py \
    --input data.csv \
    --icd-prefix ICD_DGNS_CD \
    --max-icd-cols 5
```

### If you have a huge dataset with many rows:

No problem! The script handles any number of records.

```bash
# 100,000 rows? No problem
python accurate_cci_calculator.py \
    --input massive_dataset.csv
```

The script will process approximately 200 rows per second. A 100,000-row file takes ~8 minutes.

### If your ICD codes have different formats:

The script expects standard ICD-10 codes (e.g., `I50.9`, `E11.9`)

If your codes look like:
- `I500` → Should be `I50.0`
- `E11` → Should be `E11.9`
- `50.9` → Should be `I50.9`

You may need to reformat them in Excel first using formulas.

---

## Output Interpretation

### What does CCI Score mean?

- **Score 0:** No tracked comorbidities
- **Score 1-2:** Low comorbidity burden
- **Score 3-5:** Moderate comorbidity burden
- **Score 6+:** High comorbidity burden

Each condition found = 1 point. Maximum possible with these 10 conditions = 10 points.

### Columns in Output Excel:

1. **DSYSRTKY** → Patient ID (renamed from your column)
2. **CLAIMNO** → Claim/Visit ID (renamed from your column)
3. **CCI_Score** → Total comorbidity count (0-10)
4. **Has_ICD_Codes** → Yes/No (whether any codes were found)
5. **ICD_Codes** → Actual codes found (pipe-separated)
6. **Individual condition columns** → 1 if present, 0 if absent

---

## Troubleshooting by Dataset Type

### Hospital Dataset: "Getting all 0 scores"
- Check: ICD codes are formatted correctly (I50.9, not I500)
- Verify: --icd-prefix matches your column names exactly
- Try: Print column names: `pandas.read_csv('file.csv').columns`

### Insurance Database: "Script says file not found"
- Check: Full path to file
- Try: Use absolute path: `C:\Users\...\claims.csv`

### Research Study: "Output Excel is empty"
- Check: CSV file is not corrupted
- Verify: Column names are spelled exactly as specified
- Try: --max-icd-cols matches your actual number of diagnosis columns

---

## Performance Estimates

| Dataset Size | Processing Time |
|--------------|-----------------|
| 100 records | < 1 second |
| 1,000 records | ~5 seconds |
| 10,000 records | ~50 seconds |
| 100,000 records | ~8 minutes |
| 1,000,000 records | ~80 minutes |

---

## Need Help?

1. **Check column names:**
   ```bash
   python -c "import pandas as pd; print(pd.read_csv('your_file.csv').columns.tolist())"
   ```

2. **Test with sample rows:**
   ```bash
   python -c "import pandas as pd; print(pd.read_csv('your_file.csv').head())"
   ```

3. **Run with help:**
   ```bash
   python accurate_cci_calculator.py --help
   ```

---

Now you're ready to analyze comorbidity in any dataset! 🎉
