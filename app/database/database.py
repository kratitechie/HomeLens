from pathlib import Path
import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432")

if DB_HOST and DB_HOST.startswith("/cloudsql/"):
    DATABASE_URL = (
        f"postgresql+psycopg2://"
        f"{DB_USER}:{quote_plus(DB_PASSWORD)}@"
        f"/{DB_NAME}"
        f"?host={quote_plus(DB_HOST)}"
        f"&port={DB_PORT}"
    )
else:
    DATABASE_URL = (
        f"postgresql+psycopg2://"
        f"{DB_USER}:{quote_plus(DB_PASSWORD)}@"
        f"{DB_HOST}:{DB_PORT}/"
        f"{DB_NAME}"
    )

engine = create_engine(DATABASE_URL, echo=False)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(bind=engine)