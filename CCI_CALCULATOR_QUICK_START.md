# Quick Start - CCI Calculator for Any Dataset

## 30-Second Setup

### Step 1: Check Your CSV Columns
Open your CSV file and note:
- Which column has **Patient IDs** (e.g., PATIENT_ID, MRN, SUBJECT_ID)
- Which column has **Claim/Visit IDs** (e.g., CLAIM_ID, VISIT_ID, ENCOUNTER_ID)
- What **ICD code columns** look like (e.g., ICD_CODE1, ICD_CODE2, DIAGNOSIS1, DIAGNOSIS2)

### Step 2: Run the Script
```bash
python accurate_cci_calculator.py --input your_data.csv
```

### Step 3: Check Output
Open `CCI_Analysis_<timestamp>.xlsx` - done!

---

## Common Scenarios

### Scenario 1: "My columns have different names"
```bash
python accurate_cci_calculator.py \
    --input data.csv \
    --id-col PATIENT_ID \
    --claim-col VISIT_ID
```

### Scenario 2: "My ICD columns are named DIAGNOSIS1, DIAGNOSIS2, etc"
```bash
python accurate_cci_calculator.py \
    --input data.csv \
    --icd-prefix DIAGNOSIS
```

### Scenario 3: "I have only 5 ICD columns, not 12"
```bash
python accurate_cci_calculator.py \
    --input data.csv \
    --max-icd-cols 5
```

### Scenario 4: "Everything is custom"
```bash
python accurate_cci_calculator.py \
    --input data.csv \
    --id-col MRN \
    --claim-col VISIT_ID \
    --icd-prefix DIAG \
    --max-icd-cols 8 \
    --output my_results.xlsx
```

---

## What You Get

An Excel file with 4 sheets:
1. **CCI Results** - All patients with scores
2. **Condition Detection** - How many patients have each condition
3. **Summary Statistics** - Overall statistics
4. **Detailed Analysis** - Detailed patient breakdown

---

## CSV Format Example

Your file should look like:
```
PATIENT_ID,VISIT_ID,DIAG1,DIAG2,DIAG3
101,V001,I50.9,I10,
102,V002,E11.9,I63.9,I26.99
103,V003,,,
```

**That's all!** The script handles the rest.

---

## Help Command

```bash
python accurate_cci_calculator.py --help
```

Shows all available options.

---

**Note:** Your ICD-10 codes must be in standard format (e.g., `I50.9`, `E11.9`, not `I500` or `E11`)
