from sqlalchemy.orm import Session

from app.models.property import Property


class PropertyRepository:

    def __init__(self, db: Session):
        self.db = db

    # -----------------------------
    # CREATE
    # -----------------------------

    def create(self, property_obj: Property):

        self.db.add(property_obj)
        self.db.commit()
        self.db.refresh(property_obj)

        return property_obj

    def create_many(self, properties: list[Property]):

        self.db.add_all(properties)
        self.db.commit()

        return len(properties)

    # -----------------------------
    # READ
    # -----------------------------

    def get_all(self):

        return self.db.query(Property).all()

    def get_by_property_id(self, property_id: str):

        return (
            self.db.query(Property)
            .filter(Property.property_id == property_id)
            .first()
        )

    def find_by_location(self, location: str):

        return (
            self.db.query(Property)
            .filter(Property.location.ilike(f"%{location}%"))
            .all()
        )

    # -----------------------------
    # UPDATE
    # -----------------------------

    def update(self, property_id: str, updates: dict):

        property_obj = self.get_by_property_id(property_id)

        if property_obj is None:
            return None

        for key, value in updates.items():
            setattr(property_obj, key, value)

        self.db.commit()
        self.db.refresh(property_obj)

        return property_obj

    # -----------------------------
    # DELETE
    # -----------------------------

    def delete(self, property_id: str):

        property_obj = self.get_by_property_id(property_id)

        if property_obj is None:
            return False

        self.db.delete(property_obj)
        self.db.commit()

        return True