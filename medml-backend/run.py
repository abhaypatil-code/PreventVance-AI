import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))
app_dir = os.path.join(basedir, 'app')
db_path = os.path.join(app_dir, 'medml.db')
os.environ.setdefault('DATABASE_URL', f'sqlite:///{os.path.abspath(db_path).replace(chr(92), "/")}')

from app import create_app

env = os.getenv('FLASK_ENV', 'development').lower()
config_name = 'production' if env == 'production' else ('testing' if env == 'testing' else 'development')
app = create_app(config_name)

if __name__ == '__main__':
    host = os.getenv('FLASK_RUN_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_RUN_PORT', '5000'))
    use_waitress = os.getenv('USE_WAITRESS', 'false').lower() in ('1', 'true', 'yes') or config_name == 'production'
    if use_waitress:
        from waitress import serve
        serve(app, host=host, port=port)
    else:
        app.run(host=host, port=port, debug=app.config.get('DEBUG', False))