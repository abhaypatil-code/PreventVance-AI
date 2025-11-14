# Manual Test Cases

Prerequisites
- Backend: `http://127.0.0.1:5000`
- Frontend: `http://127.0.0.1:8501`
- Admin: `admin` / `Admin123!`
- Patient: `12345678901234` / `12345678901234@Default123`

Test 1: Admin login
- Go to `http://127.0.0.1:8501` → login as admin
- Expect: dashboard with analytics; "Add New User" and "View Registered Patients"

Test 2: Patient registration
- From dashboard → "Add New User" → fill basics → save
- Complete 4 assessments → "Finish Survey & Run Risk Analysis"
- Expect: patient created; assessments saved; prediction triggered; patient listed

Test 3: Patient list & details
- Open patient list → view details → check tabs
- Test "Retry Prediction" and "View Latest Prediction"
- Expect: data loads; BMI/A:G correct; actions work

Test 4: Consultations & notes
- In details → book consultation for Medium/High risk → add note
- Expect: booking succeeds; notes saved and shown

Test 5: Patient login
- Logout → login with patient credentials
- Expect: dashboard, health metrics, risk table, assessment tabs, HW info, recommendations

Test 6: PDF report
- Patient dashboard → "Download PDF" → select sections → download
- Expect: PDF downloads with selected content

Test 7: Assessment history
- Patient dashboard → open assessment tabs
- Expect: tables show data; empty states handled

Test 8: Errors & edge cases
- Wrong credentials; unauthorized access; invalid ABHA; predict without assessments; backend down
- Expect: clear errors; blocked access; graceful handling

Test 9: Computed fields
- Create patient (height/weight) → verify BMI
- Liver assessment (protein/albumin) → verify A/G
- Expect: matches backend calculations

Test 10: RBAC
- Patient cannot access admin features; admin restricted from other patients
- Expect: correct gating and messages

Test 11: Prediction retry
- After failure → use retry → observe status
- Expect: informative messages; UI updates

Test 12: Session
- Idle 15+ min → actions → logout/login
- Expect: token expiry prompts; clean session

Success Criteria
- All flows work, predictions display, PDFs generate, RBAC enforced, errors clear, computed fields correct, secure session, responsive UI.

Notes
- ML models required for predictions
- PDF depends on backend config
- Recommendations need `GEMINI_API_KEY`
- Run with backend active; clean test data after testing
