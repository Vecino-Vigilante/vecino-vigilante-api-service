# Run this file to migrate tables to the database on development

from sqlmodel import SQLModel

from app.infrastructure.configs.sql_database import db_engine

# Import here one by one of the entities that you want to create within the database
from app.infrastructure.entities.user_entity import User
from app.infrastructure.entities.complaint_entity import Complaint
from app.infrastructure.entities.marker_entity import Marker
from app.infrastructure.entities.complaint_comment_entity import Comment
from app.infrastructure.entities.complaint_type_entity import ComplaintType

if __name__ == "__main__":
    SQLModel.metadata.create_all(db_engine)
