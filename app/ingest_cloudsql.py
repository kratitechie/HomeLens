import sys

sys.path.insert(0, "/app")

from app.ingestion.run_ingestion import ingest_properties


if __name__ == "__main__":
    ingest_properties()