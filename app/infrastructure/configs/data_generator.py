from uuid import UUID
from sqlmodel import Session, select
from app.infrastructure.configs.sql_database import db_engine
from app.infrastructure.entities.complaint_type_entity import ComplaintType


def add_complaint_types():
    with Session(db_engine) as session:
        if session.exec(select(ComplaintType)).first():
            return
        choque = ComplaintType(
            id=UUID("e975e7019bc847e69f8a3742cee4cf96"), name="Choque automovilístico"
        )
        sospechoso = ComplaintType(
            id=UUID("9bbb35714af649718531a700638ae4b8"), name="Persona sospechosa"
        )
        vandalismo = ComplaintType(
            id=UUID("5d2c9473e3de46ec8248650584e6fbde"), name="Vandalismo"
        )
        incendio = ComplaintType(
            id=UUID("c0f82bcc5f394abe9d13ee50bade82a8"), name="Incendio"
        )
        robo = ComplaintType(id=UUID("7b9d24cffcfe4812b6d0f0ed7f6851b4"), name="Robo")
        asalto = ComplaintType(
            id=UUID("3e5c2aa7a3914dce8a7ba73ea5596596"), name="Asalto"
        )
        session.add(choque)
        session.add(sospechoso)
        session.add(vandalismo)
        session.add(incendio)
        session.add(robo)
        session.add(asalto)
        session.commit()
