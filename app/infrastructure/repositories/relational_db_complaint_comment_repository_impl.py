from sqlmodel import Session
from app.infrastructure.configs.sql_database import db_engine
from app.application.repositories.complaint_comment_repository import ComplaintCommentRepository
from app.domain.models.complaint_comment_model import ComplaintCommentModel
from app.infrastructure.mappers.complaint_comment_mappers import map_complaint_comment_entity_to_complaint_comment_model, map_complaint_comment_model_to_complaint_comment_entity


class RelationalDBComplaintCommentRepositoryImpl(ComplaintCommentRepository):
    def add_comment(self, complaint_comment: ComplaintCommentModel) -> ComplaintCommentModel:
        with Session(db_engine) as session:
            complaint_comment_entity = map_complaint_comment_model_to_complaint_comment_entity(complaint_comment)
            session.add(complaint_comment_entity)
            session.commit()
            session.refresh(complaint_comment_entity)
            return map_complaint_comment_entity_to_complaint_comment_model(complaint_comment_entity)