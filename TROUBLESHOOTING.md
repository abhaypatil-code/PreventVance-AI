# Troubleshooting Guide

Concise fixes for common issues. Use Windows PowerShell commands.

## Quick Fixes
- Clear rate limits: `cd medml-backend; python clear_rate_limits.py`
- Recreate admin/database: `cd medml-backend; python create_admin.py`
- System check: `python test_system.py`
- Restart both services (backend and frontend)

## Rate Limiting (429)
- Clear cache: `cd medml-backend; python clear_rate_limits.py`
- Defaults: `1000/day`, `200/hour`, `50/min`; login `10/min`, registration `5/hour`

## Backend Start Issues
- Port in use: `netstat -ano | findstr :5000`; stop: `Stop-Process -Id <PID> -Force`
- Change port: `set FLASK_RUN_PORT=5001` then `python run.py`
- Install deps: `pip install -r requirements.txt`

## Database Errors
- Recreate DB: `cd medml-backend; python create_admin.py`
- Inspect file: `Get-ChildItem medml-backend/app/medml.db`
- Reset DB: `Remove-Item medml-backend/app/medml.db -Force`; then `python medml-backend/create_admin.py`

## ML Models
- Check files: `Get-ChildItem medml-backend/models_store/`
- Required: `diabetes_XGBoost.pkl`, `heart_best_model.pkl`, `liver_LightGBM SMOTE.pkl`, `mental_health_depressiveness.pkl`
- Load test:
```
cd medml-backend
python -c "from app.services import load_models; from app import create_app; app = create_app(); load_models(app)"
```

## Frontend Issues
- Backend check: `curl http://127.0.0.1:5000/api/v1/health`
- Start frontend: `cd medml-frontend; streamlit run app.py`
- Update Streamlit: `pip install streamlit --upgrade`
- Port check: `netstat -ano | findstr :8501`

## Login/Auth
- List users:
```
cd medml-backend
python -c "from app import create_app; from app.models import User; app = create_app(); app.app_context().push(); print(User.query.all())"
```
- Reset admin: `cd medml-backend; python create_admin.py`

## API/CORS
- Add frontend to `CORS_ORIGINS` in `medml-backend/.env`
- Example: `CORS_ORIGINS=http://localhost:8501,http://127.0.0.1:8501`

## Diagnostics
- Run tests: `python test_system.py`
- Backend status: `curl http://127.0.0.1:5000/api/v1/auth/me`
- DB check:
```
cd medml-backend
python -c "from app import create_app; from app.models import db; app = create_app(); app.app_context().push(); db.session.execute('SELECT 1')"
```
- Logs: check backend/terminal output

## Recovery
- Full reset:
```
Remove-Item medml-backend/app/medml.db -Force
cd medml-backend; pip install -r requirements.txt --force-reinstall
cd ../medml-frontend; pip install -r requirements.txt --force-reinstall
cd ../medml-backend; python create_admin.py
python test_system.py
```
- Restore backup:
```
Copy-Item medml-backend/app/medml.db.backup medml-backend/app/medml.db -Force
```

Always back up data before making changes.