from starlette.config import Config

config = Config()

DB_URL = config('DB_URL', str, default='sqlite://db.sqlite3')