# Streamlit Frontend Setup

Essentials to run the frontend on Windows.

## Prerequisites
- Python 3.8+
- Backend running at `http://127.0.0.1:5000`
- Database initialized; ML models in `medml-backend/models_store/`

## Install
```
cd medml-frontend
pip install -r requirements.txt
```

## Configure
Create `medml-frontend/.env`:
```
BACKEND_URL=http://127.0.0.1:5000/api/v1
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=localhost
```

## Start
```
# Backend
cd ../medml-backend
python run.py

# Frontend (new terminal)
cd ../medml-frontend
streamlit run app.py
```

## Defaults
- Admin: `admin` / `Admin123!`
- Test patient: `12345678901234` / `12345678901234@Default123`

## Tests
```
cd tests
python streamlit_frontend_checks.py
```
Manual cases: see `run_manual_checks.md`.

## Troubleshooting
- Backend connection: verify port `5000` and `BACKEND_URL`
- Auth failures: confirm admin exists; JWT keys set
- ML prediction: check model files and completed assessments
- PDF errors: ensure FPDF installed and prediction exists
- Recommendations: set `GEMINI_API_KEY`

## Debug
- Frontend logs: terminal output
- Backend debug: set `FLASK_ENV=development` and run `python run.py`

## Structure
```
medml-frontend/
├── app.py
├── api_client.py
├── utils.py
└── pages/
    ├── 1_Patient_Dashboard.py
    └── 2_Admin_Dashboard.py
```

## Production
Set in `medml-backend/.env`:
```
FLASK_ENV=production
SECRET_KEY=<secret>
JWT_SECRET_KEY=<jwt-secret>
GEMINI_API_KEY=<gemini-api-key>
DATABASE_URL=<production-db-url>
```
