from uuid import UUID
from sqlmodel import Session, select
from app.infrastructure.configs.sql_database import db_engine
from app.infrastructure.entities.complaint_type_entity import ComplaintType


def add_complaint_types():
    with Session(db_engine) as session:
        if session.exec(select(ComplaintType)).first():
            return
        choque = ComplaintType(id=UUID("e36c215e0ce211ef9f0e8e7e7d99c168"), name="Choque automovilístico")
        sospechoso = ComplaintType(id=UUID("ffa379b20ce211ef9f0e8e7e7d99c168"), name="Persona sospechosa")
        robo = ComplaintType(id=UUID("ffa4b3900ce211ef9f0e8e7e7d99c168"), name="Robo")
        asalto = ComplaintType(id=UUID("ffa59d8c0ce211ef9f0e8e7e7d99c168"), name="Asalto")
        session.add(choque)
        session.add(sospechoso)
        session.add(robo)
        session.add(asalto)
        session.commit()
        