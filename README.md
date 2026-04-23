# Verification & Validation Project – 21 CFR Atomic Rules

Group Members:
- Aidan Brinkley
- Grant Carpenter
- Blake Werk
- Vincent Cameron


## Project Overview

This project performs Verification & Validation (V&V) of regulatory requirements from 21 CFR 117.130 using Python scripts, JSON files, and GitHub Actions. Requirements are parsed from a CFR markdown file, structured into atomic units, and verified against expected test cases. Forensic logging is integrated throughout to track issues during CI.


## Inputs

- `CFR-117.130.md` — CFR section in markdown format, used as the source for all requirements
- `output1.json` — parsed list of all requirements extracted from the CFR file
- `output2.json` — expected structure mapping parent requirement IDs to their child IDs


## How to Run

**1. Generate requirements and expected structure:**
```bash
python generate_requirements.py -i "CFR-117.130.md" -o "output2.json" -c "21 CFR 117.130"
```

**2. Generate test cases:**
```bash
python generate_test_cases.py
```

**3. Run verification:**
```bash
python scripts/verify.py
```

**4. Run validation:**
```bash
python scripts/validate.py
```

CI runs steps 3 and 4 automatically on every push.


## Key Files

| File | Description |
|---|---|
| `generate_requirements.py` | Parses CFR markdown into requirements JSON |
| `generate_test_cases.py` | Generates one test case per requirement |
| `scripts/verify.py` | Verifies requirements meet structural rules |
| `scripts/validate.py` | Validates requirements match expected structure |
| `output1.json` | Full parsed requirements list |
| `output2.json` | Expected structure (parent → children) |
| `test_cases.json` | Generated test cases |
| `forensic_log.json` | Forensic event log generated during V&V runs |
| `.github/workflows/ci.yaml` | GitHub Actions CI workflow |
