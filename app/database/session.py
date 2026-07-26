from app.database.database import SessionLocal


def get_session():
    return SessionLocal()