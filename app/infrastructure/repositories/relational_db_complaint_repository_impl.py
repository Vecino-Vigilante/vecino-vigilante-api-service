from datetime import datetime
from uuid import UUID
from sqlmodel import Session, select
from app.infrastructure.configs.sql_database import db_engine
from app.application.repositories.complaint_repository import ComplaintRepository
from app.domain.models.complaint_model import ComplaintModel
from app.infrastructure.entities.complaint_entity import Complaint
from app.infrastructure.mappers.complaint_mappers import (
    map_complaint_entity_to_complaint_model,
    map_complaint_model_to_complaint_entity,
)


class RelationalDBComplaintRepositoryImpl(ComplaintRepository):
    def add_complaint(self, complaint: ComplaintModel) -> ComplaintModel:
        with Session(db_engine) as session:
            complaint_entity = map_complaint_model_to_complaint_entity(complaint)
            session.add(complaint_entity)
            session.commit()
            session.refresh(complaint_entity)
            return map_complaint_entity_to_complaint_model(complaint_entity)

    def get_complaints(
        self,
        start_date: datetime | None,
        end_date: datetime | None,
        type_id: UUID | None,
    ):
        with Session(db_engine) as session:
            query = select(Complaint)
            if start_date:
                query = query.where(Complaint.date >= start_date)
            if end_date:
                query = query.where(Complaint.date <= end_date)
            if type_id:
                query = query.where(Complaint.type_id == type_id)
            complaints = session.exec(query).all()
            return [map_complaint_entity_to_complaint_model(complaint) for complaint in complaints]
