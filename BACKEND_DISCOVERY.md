Concise overview of backend architecture, endpoints, ML flow, and models.

## Stack
- Flask (Flask-RESTful), SQLAlchemy + SQLite (dev)
- Auth: JWT (Flask-JWT-Extended), bcrypt
- Rate limits: Flask-Limiter
- ML: XGBoost/LightGBM via scikit-learn
- PDF: FPDF; AI: Gemini API

## Auth
- Tokens: access (15 min), refresh (30 days)
- Header: `Authorization: Bearer <token>`
- Blocklist on logout; roles: admin, patient
- Limits: login `10/min`, registration `5/hour`

## Endpoints
- Auth: `/auth/admin/login`, `/auth/patient/login`, `/auth/refresh`, `/auth/logout`, `/auth/me`
- Patients: `POST /patients`, `GET /patients`, `GET/PUT /patients/{id}`
- Assessments: `POST /patients/{id}/assessments/{type}` (diabetes, liver, heart, mental_health)
- Predictions: `POST /patients/{id}/predict`, `GET /patients/{id}/predictions/latest`
- Dashboard: `GET /dashboard/stats` (admin)
- Reports: `POST /patients/{id}/report/pdf`
- Recommendations: `GET /patients/{id}/recommendations`
- Health: `GET /health`

## ML Flow
- Models: `diabetes_XGBoost.pkl`, `heart_best_model.pkl`, `liver_LightGBM SMOTE.pkl`, `mental_health_depressiveness.pkl`
- Flow: complete 4 assessments → trigger `/predict` → scores 0–1 → levels: Low (<0.35), Medium (0.35–0.69), High (≥0.70) → store `RiskPrediction`

## Features
- Diabetes: pregnancy, glucose, blood_pressure, skin_thickness, insulin, history, age, bmi
- Heart: lifestyle, lipids, BP, pollution, family history, stress, age, gender, bmi
- Liver: bilirubin, enzymes, protein, albumin, A/G ratio
- Mental: PHQ, GAD, flags, age, gender

## Data Model
- Core: `User`, `Patient`, assessments, `RiskPrediction`, `Consultation`, `ConsultationNote`, `LifestyleRecommendation`, `TokenBlocklist`
- Computed: BMI; A/G ratio; risk levels

## Security & Validation
- Role-based access; pydantic schemas; ABHA ID (14 digits)
- Rate limits on sensitive endpoints; input sanitization

## Errors
- 422 validation, 401 auth, 403 authz, 404 not found, 409 conflict, 429 rate limit, 500 server
- ML: missing assessments, model load failures, feature mismatch

## Database
- Dev: SQLite; prod: set `DATABASE_URL` (PostgreSQL/MySQL)
- Migrations: Alembic; indexes on frequent fields