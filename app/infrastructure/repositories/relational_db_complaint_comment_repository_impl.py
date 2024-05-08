from uuid import UUID
from sqlmodel import Session, select
from app.infrastructure.entities.complaint_comment_entity import Comment
from app.infrastructure.configs.sql_database import db_engine
from app.application.repositories.complaint_comment_repository import (
    ComplaintCommentRepository,
)
from app.domain.models.complaint_comment_model import ComplaintCommentModel
from app.infrastructure.mappers.complaint_comment_mappers import (
    map_complaint_comment_entity_to_complaint_comment_model,
    map_complaint_comment_model_to_complaint_comment_entity,
)


class RelationalDBComplaintCommentRepositoryImpl(ComplaintCommentRepository):
    def add_comment(
        self, complaint_comment: ComplaintCommentModel
    ) -> ComplaintCommentModel:
        with Session(db_engine) as session:
            complaint_comment_entity = (
                map_complaint_comment_model_to_complaint_comment_entity(
                    complaint_comment
                )
            )
            session.add(complaint_comment_entity)
            session.commit()
            session.refresh(complaint_comment_entity)
            return map_complaint_comment_entity_to_complaint_comment_model(
                complaint_comment_entity
            )

    def get_complaint_comments(self, incident_id: UUID) -> list[ComplaintCommentModel]:
        with Session(db_engine) as session:
            comments = session.exec(
                select(Comment).where(Comment.incident_id == incident_id)
            )
            return [
                map_complaint_comment_entity_to_complaint_comment_model(comment)
                for comment in comments
            ]

    def update_comment(
        self, complaint_comment: ComplaintCommentModel
    ) -> ComplaintCommentModel:
        with Session(db_engine) as session:
            comment_entity = session.get(Comment, complaint_comment.id)
            comment_entity.content = complaint_comment.content
            comment_entity.image_url = (
                complaint_comment.image_url
                if complaint_comment.image_url
                else comment_entity.image_url
            )
            session.add(comment_entity)
            session.commit()
            session.refresh(comment_entity)
            return map_complaint_comment_entity_to_complaint_comment_model(comment_entity)