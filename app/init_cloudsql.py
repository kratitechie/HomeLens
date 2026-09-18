import sys

sys.path.insert(0, "/app")

from app.database.init_db import init_db

init_db()

print("Cloud SQL database initialized successfully.")