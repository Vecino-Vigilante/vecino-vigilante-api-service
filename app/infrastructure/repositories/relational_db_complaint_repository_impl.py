from sqlmodel import Session
from app.domain.models.complaint_type_model import ComplaintTypeModel
from app.domain.models.marker_model import MarkerModel
from app.domain.models.user_model import UserModel
from app.infrastructure.configs.sql_database import db_engine
from app.application.repositories.complaint_repository import ComplaintRepository
from app.domain.models.complaint_model import ComplaintModel
from app.infrastructure.mappers.complaint_mappers import map_complaint_entity_to_complaint_model, map_complaint_model_to_complaint_entity


class RelationalDBComplaintRepositoryImpl(ComplaintRepository):
    def add_complaint(self, complaint: ComplaintModel) -> ComplaintModel:
        with Session(db_engine) as session:
            complaint_entity = map_complaint_model_to_complaint_entity(complaint)
            session.add(complaint_entity)
            session.commit()
            session.refresh(complaint_entity)
            return map_complaint_entity_to_complaint_model(complaint_entity)