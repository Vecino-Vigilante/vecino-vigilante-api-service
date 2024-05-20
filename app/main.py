from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.infrastructure.configs.sql_database import create_db_and_tables

from .infrastructure.docs.openapi_tags import openapi_tags
from .infrastructure.routers.auth_router import auth_router
from .infrastructure.routers.complaint_router import complaint_router
from .infrastructure.routers.complaint_comment_router import complaint_comment_router

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup")
    create_db_and_tables()
    yield
    print("Application shutdown")


app = FastAPI(
    title="Vecino vigilante service",
    summary="Microservice for managing complaints and comments",
    version="1.0.0",
    contact={"name": "Vecino vigilante team", "email": "vecino-vigilante@gmail.com"},
    openapi_tags=openapi_tags,
    lifespan=lifespan,
)

app.include_router(auth_router, prefix="/auth", tags=["Authorization"])
app.include_router(complaint_router, prefix="/complaints", tags=["Complaints"])
app.include_router(
    complaint_comment_router, prefix="/comments", tags=["Complaints Comments"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
