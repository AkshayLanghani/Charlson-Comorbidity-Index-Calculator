# CCI Calculator - Universal Dataset Usage Guide

## Overview
The `accurate_cci_calculator.py` script is now **fully generic** and can be applied to **ANY dataset** that contains ICD-10 diagnostic codes. It calculates the **Charlson Comorbidity Index (CCI)** using exact ICD-10 code matching.

---

## Requirements

### Python Libraries
```bash
pip install pandas numpy openpyxl
```

### Dataset Requirements
Your CSV file must contain:
- **A patient ID column** (can have any name)
- **A claim/encounter ID column** (can have any name)
- **ICD-10 diagnosis code columns** (numbered sequentially like `ICD1, ICD2, ICD3...` or `DGNS_CD1, DGNS_CD2...`)

---

## Basic Usage

### Simple Usage with Default Column Names
If your CSV file uses the standard column names:
- Patient ID column: `DSYSRTKY`
- Claim ID column: `CLAIMNO`
- ICD code columns: `ICD_DGNS_CD1`, `ICD_DGNS_CD2`, ... `ICD_DGNS_CD12`

```bash
python accurate_cci_calculator.py --input your_data.csv
```

This will generate `CCI_Analysis_<timestamp>.xlsx` automatically.

---

## Advanced Usage with Custom Column Names

### Example 1: Different Column Names
If your dataset uses different column names:

```bash
python accurate_cci_calculator.py \
    --input patient_data.csv \
    --id-col PATIENT_ID \
    --claim-col ENCOUNTER_ID \
    --icd-prefix ICD_CODE \
    --output my_results.xlsx
```

This works with columns like: `ICD_CODE1`, `ICD_CODE2`, `ICD_CODE3`, etc.

### Example 2: Different Number of ICD Columns
If your dataset has only 8 ICD code columns instead of 12:

```bash
python accurate_cci_calculator.py \
    --input data.csv \
    --max-icd-cols 8 \
    --output results.xlsx
```

### Example 3: Full Customization
```bash
python accurate_cci_calculator.py \
    --input hospital_data.csv \
    --id-col MRN \
    --claim-col VISIT_ID \
    --icd-prefix DIAG \
    --max-icd-cols 15 \
    --output hospital_analysis.xlsx
```

This works with columns: `DIAG1`, `DIAG2`, ... `DIAG15`

---

## Command Line Arguments

| Argument | Short | Required | Default | Description |
|----------|-------|----------|---------|-------------|
| `--input` | `-i` | **YES** | - | Path to your CSV input file |
| `--output` | `-o` | No | `CCI_Analysis_<timestamp>.xlsx` | Path for output Excel file |
| `--id-col` | - | No | `DSYSRTKY` | Column name for patient ID |
| `--claim-col` | - | No | `CLAIMNO` | Column name for claim/encounter ID |
| `--icd-prefix` | - | No | `ICD_DGNS_CD` | Prefix for ICD code columns |
| `--max-icd-cols` | - | No | `12` | Maximum number of ICD code columns to scan |

---

## Usage Examples

### Medical Center Dataset
```bash
python accurate_cci_calculator.py \
    --input medical_center_patients.csv \
    --id-col MEDICAL_RECORD_NUMBER \
    --claim-col ADMISSION_ID
```

### Insurance Claims Data
```bash
python accurate_cci_calculator.py \
    --input claims_database.csv \
    --id-col MEMBER_ID \
    --claim-col CLAIM_ID \
    --icd-prefix DIAGNOSIS
```

### Research Dataset
```bash
python accurate_cci_calculator.py \
    --input research_cohort.csv \
    --id-col SUBJECT_ID \
    --claim-col EPISODE_ID \
    --icd-prefix ICD10 \
    --max-icd-cols 20 \
    --output research_comorbidity_results.xlsx
```

---

## Input Data Format

### Minimal Example
Your CSV file should look like this:

```
DSYSRTKY,CLAIMNO,ICD_DGNS_CD1,ICD_DGNS_CD2,ICD_DGNS_CD3
PAT001,CLM001,I50.9,I10,
PAT002,CLM002,E11.9,I63.9,I26.99
PAT003,CLM003,,,
```

### With Custom Column Names
```
MRN,VISIT_ID,DIAG1,DIAG2,DIAG3,DIAG4
12345,V001,I50.22,I10,I25.10,
12346,V002,E11.9,,G45.9,I70.0
12347,V003,,,
```

---

## Output Files

### Excel Workbook Contains 4 Sheets:

#### 1. **CCI Results (All X Patients)**
- Complete list of all patients with their CCI scores
- Shows patient ID, claim ID, CCI score, presence of codes, and actual codes found

#### 2. **Condition Detection**
- Summary table showing:
  - How many patients have each condition
  - Percentage of patients with each condition
  - The exact ICD-10 codes being matched

#### 3. **Summary Statistics**
- Overall statistics including:
  - Total number of patients
  - Patients with codes
  - Mean, median, min, max CCI scores
  - Standard deviation
  - Method information

#### 4. **Detailed Analysis**
- Detailed view showing first 100 patients
- Columns for each condition (0 or 1 indicating presence/absence)
- Color-coded for easy reading

---

## Tracked Conditions

The calculator tracks **10 comorbidity conditions**:

| Condition | ICD-10 Codes | Points |
|-----------|--------------|--------|
| Chronic Heart Failure (CHF) | I50.22, I50.32, I50.42, I50.9 | 1 |
| Hypertension | I10 | 1 |
| Stroke/Cerebrovascular | I63.9 | 1 |
| Transient Ischemic Attack (TIA) | G45.9 | 1 |
| Thromboembolism | I26.99, I74.9, I82.409 | 1 |
| Vascular Disease | I25.10, I70.0, I73.9 | 1 |
| Myocardial Infarction | I25.2, I21.9 | 1 |
| Peripheral Artery Disease | I73.9, I70.2 | 1 |
| Diabetes Mellitus | E11.9 | 1 |
| Aortic Plaque/Atherosclerosis | I70.0 | 1 |

**Note:** CCI Score = Sum of all conditions found (each condition = 1 point)

---

## How the Script Works

1. **Loads your CSV file** with the specified patient and claim ID columns
2. **Extracts ICD-10 codes** from the diagnosis columns
3. **Matches codes exactly** (no partial matching) against the 10 tracked conditions
4. **Calculates CCI score** as the count of present conditions
5. **Generates Excel report** with results, statistics, and condition details

---

## Troubleshooting

### Error: "Column 'X' not found in dataset"
**Solution:** Check your CSV file column names match what you specified with `--id-col` and `--claim-col`

**Command to check available columns:**
```bash
python -c "import pandas as pd; df = pd.read_csv('your_data.csv'); print(df.columns.tolist())"
```

### Error: "Input file not found"
**Solution:** Verify the full path to your CSV file is correct. Use absolute path if relative path doesn't work.

```bash
# Windows example
python accurate_cci_calculator.py --input "C:\Users\YourName\Documents\data.csv"

# Linux/Mac example
python accurate_cci_calculator.py --input "/home/user/documents/data.csv"
```

### No output Excel file created
**Solution:** Check that you have write permissions in the output directory. If using `--output`, ensure the directory exists.

### CCI scores all 0 or NaN
**Solution:** Verify:
1. Your ICD code columns contain actual ICD-10 codes
2. The `--icd-prefix` matches your actual column names
3. The ICD codes match exactly (case-insensitive, but must match the codes in the tracked list)

---

## Performance

- **Speed:** ~200 patients per second (on typical hardware)
- **Memory:** Minimal (loads entire dataset into RAM)
- **Large Datasets:** Script handles thousands of patients efficiently

---

## Support & Customization

To modify the tracked conditions or add new ones:
1. Edit the `EXACT_ICD_CODES` dictionary at the top of the script
2. Add new conditions with their ICD-10 codes and point values
3. Re-run the script

Example:
```python
EXACT_ICD_CODES = {
    'NEW_CONDITION': {
        'name': 'New Condition Name',
        'codes': ['ICD10.1', 'ICD10.2'],
        'points': 1
    },
    # ... rest of conditions
}
```

---

## Version History

**v2.0** - Universal Multi-Dataset Support
- Added command-line argument support
- Works with any dataset
- Customizable column names and ICD prefix
- Dynamic output naming

**v1.0** - Original 839-patient dataset version

---

## Questions?

Ensure your CSV file has:
- Patient ID column (name it whatever you want, just tell the script)
- Claim ID column (same flexibility)
- ICD-10 diagnosis codes (sequential columns with consistent prefix)
- Codes in standard ICD-10 format (e.g., I50.9, E11.9, not I500 or E11)

Then run:
```bash
python accurate_cci_calculator.py --input your_file.csv --id-col YOUR_ID_COL --claim-col YOUR_CLAIM_COL
```

That's it!
