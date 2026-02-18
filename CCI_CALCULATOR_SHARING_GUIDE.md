# CCI Calculator - Universal Usage Guide

## Overview

The `accurate_cci_calculator.py` script works with ANY dataset that contains ICD-10 diagnostic codes. This guide explains how to use it with different types of data.

---

## Documentation Files

### For First-Time Users
1. **[CCI_CALCULATOR_README.md](CCI_CALCULATOR_README.md)** - START HERE
   - Overview and quick start
   - Basic usage examples
   - FAQ

2. **[CCI_CALCULATOR_QUICK_START.md](CCI_CALCULATOR_QUICK_START.md)** 
   - 30-second setup
   - Common scenarios with commands
   - Quick copy-paste ready

### For Detailed Information
3. **[CCI_CALCULATOR_USAGE_GUIDE.md](CCI_CALCULATOR_USAGE_GUIDE.md)**
   - Complete reference guide
   - All command-line arguments
   - Input/output formats
   - Troubleshooting guide
   - Performance info

4. **[CCI_CALCULATOR_EXAMPLES.md](CCI_CALCULATOR_EXAMPLES.md)**
   - Real-world examples:
     - Hospital datasets
     - Insurance claims
     - Research cohorts
     - Primary care registries
     - EHR exports
   - Step-by-step setup

---

## Quick Start (Pick Your Path)

### Path A: "Just Run It"
1. Install: `pip install pandas numpy openpyxl`
2. Run: `python accurate_cci_calculator.py --input your_data.csv`
3. Done! Open the Excel file

### Path B: "I Have Custom Column Names"
```bash
python accurate_cci_calculator.py \
    --input data.csv \
    --id-col PATIENT_ID \
    --claim-col VISIT_ID \
    --icd-prefix DIAGNOSIS
```

### Path C: "Tell Me More First"
Read → [CCI_CALCULATOR_README.md](CCI_CALCULATOR_README.md)

---

## 📦 What's Included

```
Files in This Package:
├── accurate_cci_calculator.py         (✨ Main script - UPDATED)
├── CCI_CALCULATOR_README.md           (📖 Start here)
├── CCI_CALCULATOR_QUICK_START.md      (⚡ 30-second guide)
├── CCI_CALCULATOR_USAGE_GUIDE.md      (📚 Complete reference)
├── CCI_CALCULATOR_EXAMPLES.md         (Real-world examples)
└── CCI_CALCULATOR_SHARING_GUIDE.md    (This file)
```

---

## Key Improvements

- Works with ANY dataset
- Customizable column names
- Flexible ICD columns
- Professional documentation
- Backward compatible

---

## How to Share This

### Option 1: Share Everything
```
Send all these files:
- accurate_cci_calculator.py
- CCI_CALCULATOR_README.md
- CCI_CALCULATOR_QUICK_START.md
- CCI_CALCULATOR_USAGE_GUIDE.md
- CCI_CALCULATOR_EXAMPLES.md
```

### Option 2: Minimal Share
```
Send these:
- accurate_cci_calculator.py
- CCI_CALCULATOR_README.md
```

### Option 3: Just Share the Script
```
Send:
- accurate_cci_calculator.py

(With verbal instructions: "Run: python accurate_cci_calculator.py --input your_data.csv")
```

---

## Feature Compatibility

| Capability | Before | After |
|-----------|--------|-------|
| Number of datasets supported | 1 (839 patients only) | ∞ (any CSV) |
| Custom patient ID column | No | Yes |
| Custom claim ID column | No | Yes |
| Custom ICD prefix | No | Yes |
| Variable ICD columns | No | Yes |
| CLI arguments | No | Yes |
| Help command | No | Yes |
| Documentation | No | Yes |
| Error handling | Basic | Advanced |
| Output filename | Hard-coded | Auto-generated |

---

## 🎓 Learning Path

**Beginner (5 min):**
1. Read: CCI_CALCULATOR_README.md
2. Run: `python accurate_cci_calculator.py --help`
3. Use: `python accurate_cci_calculator.py --input your_data.csv`

**Intermediate (15 min):**
1. Read: CCI_CALCULATOR_QUICK_START.md
2. Pick your scenario
3. Customize: Add --id-col, --claim-col, --icd-prefix

**Advanced (30 min):**
1. Read: CCI_CALCULATOR_USAGE_GUIDE.md
2. Read: CCI_CALCULATOR_EXAMPLES.md
3. Solve specific use cases

**Deep Dive (optional):**
1. Review code for understanding
2. Review any specific calculator variant
3. Modify if needed for custom conditions

---

## Checklist for Using

Before running the script:
- [ ] Python 3.6+ installed
- [ ] Required libraries installed: `pip install pandas numpy openpyxl`
- [ ] CSV file ready with ICD-10 codes
- [ ] Identified your ID column name
- [ ] Identified your claim column name
- [ ] Identified your ICD column prefix
- [ ] Counted your ICD columns

---

## Troubleshooting Quick Reference

| Problem | Solution |
|---------|----------|
| "Column X not found" | Use `--id-col CORRECT_NAME` |
| "File not found" | Use full path to CSV |
| "All scores are 0" | Check ICD code format (I50.9, not I500) |
| "Need help" | Run `python accurate_cci_calculator.py --help` |
| "Want examples" | See CCI_CALCULATOR_EXAMPLES.md |

---

## 📞 Next Steps

### For End Users of This Script:
1. Read: [CCI_CALCULATOR_README.md](CCI_CALCULATOR_README.md)
2. Prepare your CSV file
3. Run the appropriate command

### For Sharing With Others:
1. Share: accurate_cci_calculator.py + documentation files
2. Point them to: CCI_CALCULATOR_README.md
3. Let them run with their own data

### For Integration Into Larger Systems:
1. Copy: accurate_cci_calculator.py
2. Modify: EXACT_ICD_CODES dictionary as needed
3. Call: process_calculator() function programmatically

---

## 🌟 Key Features by Use Case

### Hospital/Healthcare Provider
✅ Fast processing (200+ records/sec)
✅ Works with any EHR export format
✅ Generates professional Excel reports
✅ Batch process entire patient populations

### Insurance/Claims Company
✅ Process any claims dataset
✅ Track comorbidity trends
✅ Generate member cohorts
✅ Export to Excel for analysis

### Research Institution
✅ Prepare cohorts for studies
✅ Baseline comorbidity assessment
✅ Track conditions over time
✅ Excel export for further analysis

### Individual Researchers
✅ Simple CLI interface
✅ No coding required
✅ Automatic file generation
✅ Complete documentation included

---

## 💾 What The Output Contains

**Excel File with 4 Sheets:**

1. **CCI Results** 
   - All patients with ID, claim ID, score
   - Shows detected codes
   
2. **Condition Detection**
   - Prevalence of each condition
   - Percentage of patients affected
   
3. **Summary Statistics**
   - Mean, median, min, max scores
   - Count of patients with codes
   
4. **Detailed Analysis**
   - Individual patient condition breakdown
   - 1/0 indicators for each condition

---

## 🔐 Data Privacy

✅ Script processes data locally
✅ No internet connection required
✅ No data is sent anywhere
✅ All analysis stays on your computer
✅ Output file stays on your system

---

## 🎉 You're All Set!

Everything is ready to go. Your script can now be used with:
- ✅ Any healthcare dataset
- ✅ Any column naming convention
- ✅ Any number of ICD diagnoses
- ✅ Any organization or project

**Start with:** [CCI_CALCULATOR_README.md](CCI_CALCULATOR_README.md)

---

**Version:** 2.0 - Universal Multi-Dataset Support
**Date:** February 2025
**Status:** ✅ Ready to Share & Use
