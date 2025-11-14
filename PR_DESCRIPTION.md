# PR: Streamlit Frontend Completion

Complete admin and patient flows with full backend and ML integration.

## Highlights
- Auth: JWT, role-based UI, secure session handling
- Admin: dashboard, patient registration, 4 assessments, consultations, notes, prediction retry
- Patient: dashboard, assessment history, risk display, recommendations, PDF reports
- Computed fields: BMI, A/G ratio (frontend ≅ backend formulas)
- Robust error handling across API and ML

## Files
- Frontend: `medml-frontend/api_client.py`, `pages/1_Patient_Dashboard.py`, `pages/2_Admin_Dashboard.py`
- New: `backend_routes_map.json`, `BACKEND_DISCOVERY.md`, `tests/streamlit_frontend_checks.py`, `run_manual_checks.md`, `CHANGELOG_STREAMLIT.md`, `setup_frontend.md`

## Validation
```
# Backend
cd medml-backend
python run.py

# Frontend
cd ../medml-frontend
streamlit run app.py

# Automated tests
cd ../tests
python streamlit_frontend_checks.py
```
Manual flows: see `run_manual_checks.md`.

## Config
- Env vars: `SECRET_KEY`, `JWT_SECRET_KEY`, `GEMINI_API_KEY`
- Models: files in `medml-backend/models_store/`

## Limitations
- Predictions depend on model files
- Recommendations require `GEMINI_API_KEY`
- Token expiry ~15 min (configurable)

## Security & Performance
- JWT, RBAC, sanitized inputs, clear error messages
- Efficient API usage, responsive UI, minimal reloads
