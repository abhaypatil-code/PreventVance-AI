# Comprehensive Test Data Generator

Creates realistic dummy data for testing: one admin and 50+ patients.

## Features
- Admin user + diverse patient demographics
- Four assessments per patient (diabetes, liver, heart, mental health)
- Balanced risk level distribution (Low/Medium/High)
- Automatic risk predictions and sample consultations/notes

## Usage
```
cd medml-backend
python comprehensive_test_data_generator.py
python verify_test_data.py
```

## Generated Data
- Admin: `admin@healthcare.com` / `Admin123!`
- Patients: ~50, password `Patient123!`
- Sample risk distribution:
  - Diabetes: 70% Low, 30% High
  - Heart: 44% Low, 26% Medium, 30% High
  - Liver: 74% Low, 26% High
  - Mental Health: 48% Low, 14% Medium, 38% High

## Tables Populated
- `users`, `patients`, all assessment tables, `risk_predictions`, `consultations`, `consultation_notes`

## Notes
- Clears existing data before generation
- Strong passwords; unique 14-digit ABHA IDs
- Risk scores use realistic medical thresholds
